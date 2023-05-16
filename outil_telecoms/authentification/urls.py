from unicodedata import name
from django.urls import include,path

from authentification.views import login, login_view

urlpatterns = [
    path('',login,name='login'),
    path('authentification',login_view,name="authentification")
]