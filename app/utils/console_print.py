from rich import print as rich_print
from rich.tree import Tree


def print_console(exc: Exception, request: object, response: object) -> None:
    """print **request exception** in terminal for better understanding

    Args:
        exc (Exception): exception
        request (object): request object
    """
    error_request_tree = Tree("[bold]EXCEPTION INFO[bold]", guide_style="bold bright_black")

    error_tree = error_request_tree.add("[bold]EXCEPTION[bold]", guide_style="bright_black")
    request_info = error_request_tree.add("[bold]REQUEST_DETAIL[bold]", guide_style="bright_black")
    response_info = error_request_tree.add("[bold]RESPONSE_DETAIL[bold]", guide_style="bright_black")

    method = getattr(request, "method", None)
    request_path = request.get_full_path()
    request_data = getattr(request, "data", None)
    request_headers = getattr(request, "headers", None)
    query_params = [f"{k}: {v}" for k, v in request.GET.items()]
    query_params = query_params if query_params else ""

    error_tree.add(str(exc))
    request_info.add(f"METHOD: {method}")
    request_info.add(f"PATH: {request_path}")
    request_info.add(f"DATA: {request_data}")
    request_info.add(f"HEADERS: {request_headers}")
    request_info.add(f"PARAMS: {query_params}")

    response_info.add(f"RESPONSE {response}")

    rich_print(error_request_tree)
