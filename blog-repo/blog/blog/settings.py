import os
from dotenv import load_dotenv

load_dotenv()

DJANGO_ENV = os.getenv('DJANGO_ENV','development')

if DJANGO_ENV == 'production':
    from .configurations.production import *
else:
    from .configurations.local import *

# Redirigir al home después del login
LOGIN_REDIRECT_URL = 'home'
# Redirigir al home después del logout (o al login si prefieres)
LOGOUT_REDIRECT_URL = 'home'

STATIC_URL = '/static/'


STATICFILES_DIRS = [
   # BASE_DIR / "static",
    
     os.path.join(BASE_DIR, 'static'),
]