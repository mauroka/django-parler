from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

admin.autodiscover()

# Patterns are prefixed with the language code.
# This is not mandatory, can also use a `django_language` cookie,
# or custom middleware that calls `django.utils.translation.activate()`.
urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('article.urls')),
)
