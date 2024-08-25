from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response
from rest_framework.views import exception_handler

from app.utils.console_print import print_console


def error_handler(exc, context) -> Response:
    response: Response | None = exception_handler(exc, context)

    if response is not None:
        if response.status_code in [405, 429, 403]:
            print_console(exc=exc, request=context["request"], response=response)
            return Response({"data": [], "success": False, "message": _("INVALID_REQUEST")}, status=403)
        return response

    print_console(exc=exc, request=context["request"], response=response)
    return Response({"data": [], "success": False, "message": _("EXCEPTION")}, status=500)
