from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("register", views.register, name="register"),
    path("login", views.my_login, name="login"),
    path("logout", views.my_logout, name="logout"),
    path("dash", views.dashboard, name="dashboard"),
    path("create_record", views.create_record, name="create_record"),
    path("record/<int:pk>", views.single_record, name="record"),
    path("delete/<int:pk>", views.delete_record, name="delete"),
    path("update_record/<int:pk>", views.update_record, name="update_record"),
]
