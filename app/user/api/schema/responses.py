from app.core.base_classes.serializer import ResponseSchemaSerializer
from app.user.api.serializers import UserRetrieveSerializer


class UserResponseSerializer(ResponseSchemaSerializer):
    result = UserRetrieveSerializer()
