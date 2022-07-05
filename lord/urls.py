from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("csgo/", include(("csgo.urls", "csgo"), namespace="csgo")),
    path("valorant/", include(("valor.urls", "valor"), namespace="valor")),
    path("", include(("globalapp.urls", "globalapp"), namespace="globalapp")),
    path("", include(("news_app.urls", "news_app"), namespace="news_app")),
    path("", include(("base_app.urls", "base_app"), namespace="base_app")),
    path("", include(("commerce.urls", "commerce"), namespace="commerce")),
    path("summernote/", include("django_summernote.urls")),
    path("filer/", include("filer.urls")),
    path('django-jsonform/', include('django_jsonform.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
