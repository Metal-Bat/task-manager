from typing import Any

from rest_framework import status as response_status
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer


def match_status(status: int) -> tuple[bool, object]:
    """match status and success base on response

    Args:
        status (int): selected status code

    Raises:
        ValueError: if status is not correct

    Returns:
        tuple[bool, object]: success and response status code object
    """
    match status:
        case 200:
            status: response_status = response_status.HTTP_200_OK
            success: bool = True
        case 400:
            status = response_status.HTTP_400_BAD_REQUEST
            success: bool = False
        case 403:
            status = response_status.HTTP_403_FORBIDDEN
            success: bool = False
        case 404:
            status = response_status.HTTP_404_NOT_FOUND
            success: bool = False
        case 500:
            status = response_status.HTTP_500_INTERNAL_SERVER_ERROR
            success: bool = False
        case _:
            raise ValueError("invalid status")
    return success, status


def response_formatter(
    result: list | dict | None = None,
    status: int = 200,
    message: dict | None = None,
    error_code: int = 0,
) -> Response:
    """response manger for all requests

    Args:
        result (list | dict | None, optional): data for response. Defaults to None.
        status (int, optional): status of response. Defaults to 200.
        message (dict | None, optional): message of response. Defaults to None.
        error_code (int, optional): error_code of response. Defaults to 0.



    Returns:
        Response: standard response
    """

    if result is None:
        result = {}

    if message is None:
        message = {}

    success, status = match_status(status)

    response: dict[str, Any] = {
        "result": result,
        "success": success,
        "message": message,
        "error_code": error_code,
    }
    return Response(response, status=status)


def paginated_data(
    request: Request,
    serializer: Serializer,
    queryset: object,
    page_size: int = 10,
) -> Response:
    """core place for paginated data to return to user

    Args:
        request (Request): user request
        serializer (Serializer): serializer for this object
        queryset (object): selected queryset
        page_size (int, optional): page size. Defaults to 10.

    Returns:
        object: user paginated response
    """
    paginator = PageNumberPagination()
    paginator.page_size = page_size
    paginated_queryset: None | list[Any] = paginator.paginate_queryset(queryset, request)
    serialized_data: Any = serializer(paginated_queryset, many=True)
    paginated_response: Response = paginator.get_paginated_response(serialized_data.data)
    return paginated_response
