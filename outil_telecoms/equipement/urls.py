from django.urls import path

from equipement.views import AffectationListView, BcCreateView, BcDeleteView, BcUpdateView, BcView, CreateStockView, ModeleCreateView, ModeleDeleteView, ModeleUpdateView, ModeleView, Reception_articleCreateView, Reception_articleDeleteView, Reception_articleUpdateView, Reception_articleView, Type_equipementCreateView, Type_equipementDeleteView, Type_equipementUpdateView, Type_equipementView, affect_stock_equipement_view, autocomplete_bc, equipement, get_materiel, reception_stock_equipement_view, stock_equipement_view, update_stock_equipement_view

urlpatterns = [
    path('', equipement,name='equipement'),
    path('create-stock/', CreateStockView.as_view(), name='create_stock'),
    path('get_materiel/', get_materiel, name='get_materiel'),
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
    path('stock_equipement/', stock_equipement_view , name='stock_equipement'),
    path('affect_equipement/', affect_stock_equipement_view , name='affect_stock_equipement_view'),
    path('reception_equipement/', reception_stock_equipement_view , name='reception_stock_equipement_view'),
    path('autocomplete_bc/', autocomplete_bc ,name='autocomplete_bc'),
    path('affectations/update/<int:id_affectation>/', update_stock_equipement_view , name='update_affectation'),
    path('affectations/', AffectationListView.as_view(), name='affectation_list'),

    
]