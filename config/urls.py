from django.conf import settings
from django.conf.urls import handler403, handler404, handler500
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.urls.resolvers import URLPattern, URLResolver
from rest_framework_simplejwt.views import TokenBlacklistView, TokenObtainPairView, TokenRefreshView, TokenVerifyView

from config.api_doc import schema_view

urlpatterns: list[URLPattern | URLResolver] = i18n_patterns(
    # admin
    path(settings.ADMIN_URL, admin.site.urls),  # type: ignore[misc]
    # api documentation
    path("swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    # simple jwt authentication
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/v1/token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
    # app services
    path(r"api/v1/", include("app.urls")),
    # static files
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        django_toolbar_url: list[URLResolver] = [path("__debug__/", include(debug_toolbar.urls))]
        urlpatterns = django_toolbar_url + urlpatterns

else:
    handler403 = "config.response_handler.custom_403_handler"  # noqa: F811
    handler404 = "config.response_handler.custom_404_handler"  # noqa: F811
    handler500 = "config.response_handler.custom_500_handler"  # noqa: F811
