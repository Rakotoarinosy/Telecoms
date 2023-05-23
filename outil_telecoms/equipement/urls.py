from django.urls import path

from equipement.views import ModeleCreateView, ModeleDeleteView, ModeleUpdateView, ModeleView, Type_equipementCreateView, Type_equipementDeleteView, Type_equipementUpdateView, Type_equipementView, equipement

urlpatterns = [
    path('', equipement,name='equipement'),
    #PARAMETRAGE
    ##paramètrage équipement
    ###type_equipement
    path('type_equipement/', Type_equipementView.as_view(), name='type_equipement'),
    path('create_type_equipement/', Type_equipementCreateView.as_view(),name='create_type_equipement'),
    path('type_equipement/<int:pk>/update/', Type_equipementUpdateView.as_view(), name='update_type_equipement'),
    path('type_equipement/<int:pk>/delete/',Type_equipementDeleteView.as_view(), name='delete_type_equipement'),
    ###modele
    path('modele/', ModeleView.as_view(), name='modele'),
    path('create_modele/', ModeleCreateView.as_view(),name='create_modele'),
    path('modele/<int:pk>/update/', ModeleUpdateView.as_view(), name='update_modele'),
    path('modele/<int:pk>/delete/',ModeleDeleteView.as_view(), name='delete_modele'),
]