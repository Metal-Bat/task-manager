from django.utils.translation import gettext_lazy as _
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title=_("PROJECT_API_TITLE"),
        default_version="v1",
        description=_("PROJECT_API_DESCRIPTION"),
        contact=openapi.Contact(email="erfan.ehsany@outlook.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    url="http://127.0.0.1:8000/en",
)
