from app.core.base_classes.serializer import BaseSerializer
from app.task.models import Sprint, Task
from app.user.models import User


class SprintListSerializer(BaseSerializer):
    """Sprint info serializer"""

    class Meta:
        model = Sprint
        fields: list[str] = BaseSerializer.Meta.fields + [
            "title",
            "state",
        ]


class SprintCreateSerializer(BaseSerializer):
    class Meta:
        model = Sprint
        fields: list[str] = [
            "title",
            "state",
        ]


class SprintTaskRetrieveSerializer(BaseSerializer):
    """Task for sprint info serializer"""

    class Meta:
        model = Sprint
        fields: list[str] = BaseSerializer.Meta.fields + [
            "title",
            "state",
        ]


class SprintRetrieveSerializer(BaseSerializer):
    """Sprint info serializer"""

    tasks = SprintTaskRetrieveSerializer(many=True)

    class Meta:
        model = Sprint
        fields: list[str] = BaseSerializer.Meta.fields + [
            "title",
            "state",
            "tasks",
        ]


class SprintUpdateSerializer(BaseSerializer):
    """Sprint update serializer"""

    class Meta:
        model = Sprint
        fields: list[str] = [
            "title",
            "state",
        ]


class SprintPartialUpdateSerializer(BaseSerializer):
    """Sprint partial update serializer"""

    class Meta:
        model = Sprint
        fields: list[str] = [
            "title",
            "state",
        ]


class TaskSprintSerializer(BaseSerializer):
    """Sprint data for task serializer"""

    class Meta:
        model = Sprint
        fields: list[str] = BaseSerializer.Meta.fields + [
            "title",
            "state",
        ]


class TaskListSerializer(BaseSerializer):
    """Task info serializer"""

    class Meta:
        model = Task
        fields: list[str] = BaseSerializer.Meta.fields + [
            "title",
            "state",
            "due_date",
            "assigned_to",
            "reviewed_by",
        ]


class TaskCreateSerializer(BaseSerializer):
    class Meta:
        model = Task
        fields: list[str] = [
            "sprint",
            "title",
            "state",
            "assigned_to",
            "reviewed_by",
            "due_date",
        ]


class TaskUpdateSerializer(BaseSerializer):
    class Meta:
        model = Task
        fields: list[str] = [
            "sprint",
            "title",
            "state",
            "assigned_to",
            "reviewed_by",
            "due_date",
        ]


class TaskPartialUpdateSerializer(BaseSerializer):
    class Meta:
        model = Task
        fields: list[str] = [
            "sprint",
            "title",
            "state",
            "assigned_to",
            "reviewed_by",
            "due_date",
        ]


class UserInfoSerializer(BaseSerializer):
    """User info serializer"""

    class Meta:
        model = User
        fields: list[str] = BaseSerializer.Meta.fields + [
            "first_name",
            "last_name",
            "avatar",
            "mobile",
            "email",
            "username",
        ]


class TaskInfoSerializer(BaseSerializer):
    """Task info serializer"""

    sprint = TaskSprintSerializer(read_only=True)
    assigned_to = UserInfoSerializer(read_only=True)
    reviewed_by = UserInfoSerializer(read_only=True)

    class Meta:
        model = Task
        fields: list[str] = BaseSerializer.Meta.fields + [
            "title",
            "state",
            "due_date",
            "assigned_to",
            "reviewed_by",
            "sprint",
        ]
