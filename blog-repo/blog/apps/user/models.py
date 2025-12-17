from django.db import models
from django.contrib.auth.models import AbstractUser, Group
import uuid
import os
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver


# --- Función para generar nombre dinámico del avatar ---
def get_avatar_filename(instance, filename):
    """
    Genera un nombre único para el avatar del usuario.
    Ejemplo: user/<username>/20251216_195400.png
    """
    _, file_extension = os.path.splitext(filename)
    timestamp = now().strftime("%Y%m%d_%H%M%S")
    new_filename = f"{instance.username}_{timestamp}{file_extension}"
    return os.path.join("user/avatar/", new_filename)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alias = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(
        upload_to=get_avatar_filename,   # función, no string
        default="user/default/avatar-default.png",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username

    def get_avatar_url(self):
        """Devuelve la URL del avatar si existe."""
        if self.avatar:
            return self.avatar.url
        return "user/default/avatar-default.png"

    # --- Propiedades para verificar grupos ---
    @property
    def is_Registered(self):
        return self.groups.filter(name="Registered").exists()

    @property
    def is_Contributor(self):
        return self.groups.filter(name="Contributor").exists()

    @property
    def is_Admin(self):
        return self.groups.filter(name="Admin").exists()


# --- SIGNAL PARA ASIGNAR ROL POR DEFECTO ---
@receiver(post_save, sender=User)
def assign_default_group(sender, instance, created, **kwargs):
    """
    Asigna automáticamente el grupo 'Registered' a cada usuario nuevo,
    excepto si es superusuario.
    """
    if created and not instance.is_superuser:
        try:
            group = Group.objects.get(name="Registered")
            instance.groups.add(group)
        except Group.DoesNotExist:
            pass