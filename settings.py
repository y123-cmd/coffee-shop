# myproject/myproject/settings.py
import os

# Media files settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # This is where uploaded files will be stored
