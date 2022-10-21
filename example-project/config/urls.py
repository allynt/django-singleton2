from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from singleton2.urls import urlpatterns as singleton_urlpatterns

admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = settings.ADMIN_SITE_TITLE
admin.site.index_title = settings.ADMIN_INDEX_TITLE

urlpatterns = [
    path("admin/", admin.site.urls),
    path("singleton/", include(singleton_urlpatterns)),
    path("", include("example.urls"))
]
