from django.urls import path
from students.views import login_view


urlpatterns = [
    path("login/", login_view, name="login_view"),
]
