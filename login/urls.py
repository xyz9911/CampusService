from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^stu_login$', stu_login),
    url(r'^stu_ban$', stu_ban),
    url(r'^admin_login$', admin_login)
]
