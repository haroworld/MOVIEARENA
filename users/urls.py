from django.urls import path
from . import views


urlpatterns=[
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.Logout, name="logout"),

    path('profile/', views.profilePage, name= "profile"),
    path('edit_profile/', views.editProfile, name="edit_profile"),

    path('check_password/', views.CheckPassword, name="check_password"),
    path('change_email/', views.changeEmail, name="change_email"),
    path('check_passwordnum/', views.CheckPasswordForNum, name="check_passwordnum"),
    path('change_number/', views.changeNum, name="change_number"),
    path('change_pics/', views.changeProfilePic, name="change_pics"),

    path('settings/', views.ChangeSettings, name="settings"),
    path('delete_account/', views.DeleteAccount, name="delete_account"),

    
]