from django.urls import re_path
from user.views import home, register
from django.conf.urls import include

urlpatterns = [
    re_path(r"^home/", home, name="home"),
    re_path(r"^user/", include("django.contrib.auth.urls")),
    re_path(r"^register/", register, name="register"),
]