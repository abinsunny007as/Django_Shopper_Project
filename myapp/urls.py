from django.urls import path
from myapp import views


urlpatterns = [
    path('indexpage/', views.indexpage, name="indexpage"),
    path('add_category/', views.add_category, name="add_category"),
    path('save_category/', views.save_category, name="save_category"),
    path('display_category/', views.display_category, name="display_category"),
    path('edit_category/<int:dataid>/', views.edit_category, name="edit_category"),
    path('update_category/<int:dataid>/', views.update_category, name="update_category"),
    path('delete_category/<int:dataid>/', views.delete_category, name="delete_category"),
    path('addproduct/', views.addproduct, name="addproduct"),
    path('saveproduct/', views.saveproduct, name="saveproduct"),
    path('displayproduct/', views.displayproduct, name="displayproduct"),
    path('editproduct/<int:proid>/', views.editproduct, name="editproduct"),
    path('updateproduct/<int:proid>/', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:proid>/', views.deleteproduct, name="deleteproduct"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('Login/', views.Login, name="Login"),
    path('deletesession/', views.deletesession, name="deletesession"),
    path('display_contact/', views.display_contact, name="display_contact"),
    path('deletecontact/<int:proid>/', views.deletecontact, name="deletecontact"),
]