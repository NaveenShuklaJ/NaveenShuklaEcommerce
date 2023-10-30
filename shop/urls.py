
from django.urls import path
from . import views

urlpatterns = [
    path("", views.ShowProductView, name="ShowProductView"),
    path('login/', views.LoginPage, name="loginn"),
    path('register/', views.RegisterPage, name="registerr"),
    path('logout/', views.LogoutPage, name="logoutt"),
    path("about/", views.AboutView, name="AboutUs"),
    path("PlaceOrder/", views.PlaceOrderView, name="PlaceOrder"),
    path("cartPage/", views.CartPageView, name="cartPage"),
    path("SearchProduct/", views.SearchProductView, name="SearchProduct"),
    path("products/<int:myid>", views.DetailView, name="Productview"),
]