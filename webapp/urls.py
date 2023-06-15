from django.urls import path
from webapp import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('contactsave/', views.contactsave, name="contactsave"),
    path('cart/', views.cart, name="cart"),
    path('product/<cat_name>/', views.product, name="product"),
    path('singleproduct/<pro_id>/', views.singleproduct, name="singleproduct"),
    path('RegisterPage/', views.RegisterPage, name="RegisterPage"),
    path('saveregister/', views.saveregister, name="saveregister"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('cartpage/', views.cartpage, name="cartpage"),
    path('cartsave/', views.cartsave, name="cartsave"),
    path('deletecart/<cart_id>/', views.deletecart, name="deletecart"),
    path('checkoutpage/', views.checkoutpage, name= "checkoutpage"),
]