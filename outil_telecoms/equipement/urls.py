from django.urls import path

from equipement.views import equipement

urlpatterns = [
    path('', equipement,name='equipement'),
]