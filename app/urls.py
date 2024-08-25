from rest_framework.routers import DefaultRouter

from app.task.api.api_v1 import SprintViewSet, TaskViewSet
from app.user.api.api_v1 import UserViewSet

router = DefaultRouter()

router.register(r"user", UserViewSet, basename="user")
router.register(r"sprint", SprintViewSet, basename="sprint")
router.register(r"task", TaskViewSet, basename="task")

urlpatterns = router.urls
