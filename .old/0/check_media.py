import os
import django
from django.conf import settings
from django.views.static import serve
from django.http import HttpRequest

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

path = 'social/facebook/studiya-dizayna-saytov-i-ikh-effektivnogo-prodvizheniya_2026-03-14_14-08-25.png'
print(f"MEDIA_ROOT: {settings.MEDIA_ROOT}")
full_path = os.path.join(settings.MEDIA_ROOT, path)
print(f"Full path: {full_path}")
print(f"Exists: {os.path.exists(full_path)}")

request = HttpRequest()
try:
    response = serve(request, path, document_root=settings.MEDIA_ROOT)
    print(f"Serve status: {response.status_code}")
except Exception as e:
    print(f"Error serving: {e}")
