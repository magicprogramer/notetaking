from . import views
from django.urls import path
app_name ="authentication"
urlpatterns = [
    path("register/", views.register, name = "register"),
    path("login/<str:send_verfication>", views.login_user, name="login"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name = "logout"),
    path("profile", views.profile, name="profile"),
]