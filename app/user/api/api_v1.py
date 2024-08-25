from typing import Any

from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from app.core.base_classes.serializer import ResponseSchemaSerializer
from app.core.permission import IsActive
from app.core.response_former import response_formatter
from app.task.models import User
from app.user.api.schema.responses import UserResponseSerializer
from app.user.api.serializers import UserRetrieveSerializer


class UserViewSet(ViewSet):
    def get_permissions(self) -> list[AllowAny] | list[Any]:
        """mange permission on action **(not the best practice but small one)**"""
        return [IsActive()]

    @swagger_auto_schema(
        responses={
            "200": UserResponseSerializer(),
            "404": ResponseSchemaSerializer(),
        },
    )
    def list(self, request: Request) -> Response:
        """retrieve information of sprint"""
        user: User = request.user
        serializer: UserRetrieveSerializer = UserRetrieveSerializer(user)
        response: Response = response_formatter(serializer.data)
        return response
