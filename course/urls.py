from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.Signup, name="signup"),
    path("login/", views.UserLogin, name="login"),
    path("logout/", views.UserLogout, name="logout"),
    path("profile/", views.Profile, name="profile"),
    path("<int:id>/delete/", views.DeleteData, name="delete"),
    path("<int:id>/update/", views.update_data, name="update"),
]
