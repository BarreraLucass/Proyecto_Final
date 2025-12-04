from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import os

def avatar_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('user/avatars/', filename)

class User(AbstractUser):
    avatar = models.ImageField(upload_to=avatar_filename, null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    alias = models.CharField(max_length=30, unique=True, null=True, blank=True)

    def __str__(self):
        return self.username
    
    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return "/static/default_avatar.png"  # agregar avatar por defecto si no tiene, uno femenino, masculino y neutros.