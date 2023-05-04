from django.urls import include,path

from sim.views import test

urlpatterns = [
    path('',test,name='sim1'),
]