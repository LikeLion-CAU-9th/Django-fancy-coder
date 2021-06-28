from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from feed.views import service_landing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', service_landing, name="landing"),
    path('feed/', include('feed.urls')),
    path('chat/', include('chat.urls')),
    path('accounts/', include('accounts.urls')),
    path('group/', include('group.urls')),
    path('mapsurfing/', include('mapsurfing.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
