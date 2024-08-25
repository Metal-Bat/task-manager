from app.core.base_classes.serializer import BaseSerializer
from app.user.models import User


class UserRetrieveSerializer(BaseSerializer):
    """Sprint info serializer"""

    class Meta:
        model = User
        fields: list[str] = BaseSerializer.Meta.fields + [
            "username",
            "first_name",
            "last_name",
            "avatar",
            "description",
            "mobile",
            "email",
            "is_staff",
            "is_superuser",
            "last_login",
            "date_joined",
        ]
