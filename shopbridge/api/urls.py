from django.urls import path
from .views import ListProductsView, ProductDetailView, RegisterUsers, LoginView

urlpatterns = [ 
    path('products/', ListProductsView.as_view(), name="Products-list"),
    path('products/<int:pk>/', ProductDetailView.as_view(), name="products-detail"),
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/register/', RegisterUsers.as_view(), name="auth-register"),
]