from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myapp import views  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('upload/', views.upload_image, name='upload'),  # Upload URL
    path('gallery/', views.gallery, name='gallery'),  # Gallery URL
    path('', views.home, name='home'),  # Root URL
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)