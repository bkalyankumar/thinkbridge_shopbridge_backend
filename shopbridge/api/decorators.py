from rest_framework.response import Response
from rest_framework.views import status


def validate_request_data(fn):
    def decorated(*args, **kwargs):
        # args[0] == GenericView Object
        name = args[0].request.data.get("name", "")
        description = args[0].request.data.get("description", "")
        price = args[0].request.data.get("price", "")
        category = args[0].request.data.get("category", "")
        if not name and not description and not category:
            return Response(
                data={
                    "message": "All the fields are required to add a product"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated