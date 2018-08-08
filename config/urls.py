from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('v1/', include('v1.accounts.urls')),
    path(settings.ADMIN_URL, admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # http://www.django-rest-framework.org/topics/documenting-your-api/
    API_TITLE = 'API title'
    API_DESCRIPTION = '...'

    from rest_framework.documentation import include_docs_urls
    urlpatterns += [path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))]

    # https://github.com/bernardopires/django-tenant-schemas/issues/222
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

    # https://github.com/django-silk/silk
    if 'silk' in settings.INSTALLED_APPS:
        urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
