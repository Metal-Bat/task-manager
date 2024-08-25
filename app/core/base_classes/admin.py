from simple_history.admin import SimpleHistoryAdmin


class BaseAdminClass(SimpleHistoryAdmin):
    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions
