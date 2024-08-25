from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response

from app.core.response_former import response_formatter


def custom_403_handler(request, exception=None) -> Response:
    status: int = 403
    message: dict[str, str] = {
        "error": _("403_ERROR"),
    }
    error_code: int = 403
    response: Response = response_formatter(
        status=status,
        message=message,
        error_code=error_code,
    )
    return response


def custom_404_handler(request, exception=None) -> Response:
    status: int = 404
    message: dict[str, str] = {
        "error": _("404_ERROR"),
    }
    error_code: int = 404
    response: Response = response_formatter(
        status=status,
        message=message,
        error_code=error_code,
    )
    return response


def custom_500_handler(request, exception=None) -> Response:
    status: int = 500
    message: dict[str, str] = {
        "error": _("500_ERROR"),
    }
    error_code: int = 500
    response: Response = response_formatter(
        status=status,
        message=message,
        error_code=error_code,
    )
    return response
