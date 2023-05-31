from django.urls import path

from equipement.views import BcCreateView, BcDeleteView, BcUpdateView, BcView, CreateStockView, ModeleCreateView, ModeleDeleteView, ModeleUpdateView, ModeleView, Reception_articleCreateView, Reception_articleDeleteView, Reception_articleUpdateView, Reception_articleView, Type_equipementCreateView, Type_equipementDeleteView, Type_equipementUpdateView, Type_equipementView, equipement

urlpatterns = [
    path('', equipement,name='equipement'),
    path('create-stock/', CreateStockView.as_view(), name='create_stock'),
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
    ###bc
    path('bc/', BcView.as_view(), name='bc'),
    path('create_bc/', BcCreateView.as_view(),name='create_bc'),
    path('bc/<int:pk>/update/', BcUpdateView.as_view(), name='update_bc'),
    path('bc/<int:pk>/delete/',BcDeleteView.as_view(), name='delete_bc'),
    ###stock
    path('stock/', Reception_articleView.as_view(), name='stock'),
    path('create_stock/', Reception_articleCreateView.as_view(),name='create_stock'),
    path('stock/<int:pk>/update/', Reception_articleUpdateView.as_view(), name='update_stock'),
    path('stock/<int:pk>/delete/',Reception_articleDeleteView.as_view(), name='delete_stock'),
]