from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("csgo/", include(("csgo.urls", "csgo"), namespace="csgo")),
    path("", include(("globalapp.urls", "globalapp"), namespace="globalapp")),
    path("", include(("news_app.urls", "news_app"), namespace="news_app")),
    path("", include(("base_app.urls", "base_app"), namespace="base_app")),
    path("", include(("commerce.urls", "commerce"), namespace="commerce")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
