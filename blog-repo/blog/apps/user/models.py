from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import os
from django.conf import settings
from django.templatetags.static import static

def avatar_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('user', 'avatars', filename)

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alias = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(
        upload_to=avatar_filename,
        default='user/default/avatar-default.png',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username

    def get_avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        # Si preferís usar STATIC para el avatar por defecto:
        return static('user/default/avatar-default.png')
        # O si querés usar MEDIA:
        # return settings.MEDIA_URL + 'user/default/avatar-default.png'