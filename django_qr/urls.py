from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django_qr import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.generate_qr_codes, name='generate_qr_codes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # ← THIS LINE IS CRITICAL