from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import status
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from .models import Products
from .decorators import validate_request_data
from .serializers import ProductsSerializer,TokenSerializer,UserSerializer


# Get the JWT settings, add these lines after the import/from lines
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class ListProductsView(generics.ListAPIView):
    """
    GET products/
    POST products/
    """
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_request_data
    def post(self, request, *args, **kwargs):
        a_product = Products.objects.create(
            name=request.data["name"],
            description=request.data["description"],
            price=request.data["price"],
            category=request.data["category"]
        )
        return Response(
            data=ProductsSerializer(a_product).data,
            status=status.HTTP_201_CREATED
        )

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET products/:id/
    PUT products/:id/
    DELETE products/:id/
    """
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            a_product = self.queryset.get(pk=kwargs["pk"])
            return Response(ProductsSerializer(a_product).data)
        except Products.DoesNotExist:
            return Response(
                data={
                    "message": "Product with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_request_data
    def put(self, request, *args, **kwargs):
        try:
            a_product = self.queryset.get(pk=kwargs["pk"])
            serializer = ProductsSerializer()
            updated_product = serializer.update(a_product, request.data)
            return Response(ProductsSerializer(updated_product).data)
        except Products.DoesNotExist:
            return Response(
                data={
                    "message": "Product with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_product = self.queryset.get(pk=kwargs["pk"])
            a_product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Products.DoesNotExist:
            return Response(
                data={
                    "message": "Product with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

class LoginView(generics.CreateAPIView):
    """
    POST auth/login/
    """
    # This permission class will overide the global permission
    # class setting
    serializer_class = TokenSerializer
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class RegisterUsers(generics.CreateAPIView):
    """
    POST auth/register/
    """
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username and not password and not email:
            return Response(
                data={
                    "message": "username, password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )
        return Response(
            data=UserSerializer(new_user).data,
            status=status.HTTP_201_CREATED
        )


