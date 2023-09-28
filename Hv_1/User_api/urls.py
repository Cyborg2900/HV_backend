from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^api/user/',views.get_all_User_Data),
    re_path(r'^api/add/',views.add_user),
]
