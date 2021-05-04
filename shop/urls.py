from django.urls import path
from . import views

urlpatterns = [
    path("productlist/", views.ProductListView.as_view()),
    path("productcreate/", views.ProductCreateView.as_view()),
    path("productdetail/<int:pk>/", views.ProductDetailView.as_view()),
    path("categorylist/", views.CategoryListView.as_view()),
    path("categorydetail/<int:pk>/", views.CategoryDetailView.as_view()),
    path("categorycreate/", views.CategoryCreateView.as_view()),
]