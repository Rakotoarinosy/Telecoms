from django.urls import path
from sim.forms import TicketForm

from sim.views import *

urlpatterns = [
    path('',sim,name='sim'),
    path('home/',home,name='home'),
    path('parametrage/',parametrage,name='parametrage'),
    #SIM
    path('affectation_sim/',AffectationSimCreateView.as_view(),name='affectation_sim'),
    path('create_affectation_sim/',AffectationSimCreateView.as_view(),name='create_affectation_sim'),
    path('list_affectation_sim/',AffectationSimListView.as_view(),name='list_affectation_sim'),
    path('create_sim/',SimCreateView.as_view(),name='create_sim'),
    # path('combined-form/', CombinedFormView.as_view(), name='combined_form_view'),
    # path('combined-form/', combined_form_view, name='combined_form_view'),
    #auto complète
    path('get_forfait/', get_forfait, name='get_forfait'),
    path('get_collaborateur/', get_collaborateur, name='get_collaborateur'),
    #PARAMETRAGE
    ##paramètrage sim
    ###profil
    path('create_profil/', ProfilCreateView.as_view(), name='create_profil'),
    path('list_profil/', ProfilListView.as_view(), name='list_profil'),
    path('profil/<int:pk>/update/', ProfilUpdateView.as_view(), name='update_profil'),
    path('profil/<int:pk>/delete/', ProfilDeleteView.as_view(), name='delete_profil'),
    ###operateur
    path('create_operateur/', OperateurCreateView.as_view(), name='create_operateur'),
    path('list_operateur/', OperateurListView.as_view(), name='list_operateur'),
    path('operateur/<int:pk>/update/', OperateurUpdateView.as_view(), name='update_operateur'),
    path('operateur/<int:pk>/delete/', OperateurDeleteView.as_view(), name='delete_operateur'),
    ###acces
    path('create_acces/', AccesCreateView.as_view(), name='create_acces'),
    path('list_acces/', AccesListView.as_view(), name='list_acces'),
    path('acces/<int:pk>/update/', AccesUpdateView.as_view(), name='update_acces'),
    path('acces/<int:pk>/delete/', AccesDeleteView.as_view(), name='delete_acces'),
    ###forfait
    path('create_forfait/', ForfaitCreateView.as_view(), name='create_forfait'),
    path('list_forfait/', ForfaitListView.as_view(), name='list_forfait'),
    path('forfait/<int:pk>/update/', ForfaitUpdateView.as_view(), name='update_forfait'),
    path('forfait/<int:pk>/delete/', ForfaitDeleteView.as_view(), name='delete_forfait'),
    ###type_sim
    path('create_type_sim/', Type_SimCreateView.as_view(), name='create_type_sim'),
    path('list_type_sim/', Type_SimListView.as_view(), name='list_type_sim'),
    path('type_sim/<int:pk>/update/', Type_SimUpdateView.as_view(), name='update_type_sim'),
    path('type_sim/<int:pk>/delete/', Type_SimDeleteView.as_view(), name='delete_type_sim'),
    #division
    # path('type_sim/',Type_SimCreateView.as_view(),name='type_sim_create_and_list'),
    # path('division/<int:pk>/delete/', DivisionDeleteView.as_view(), name='delete_division'),
    # path('division/<int:pk>/update/', DivisionUpdateView.as_view(), name='update_division'),
    # path('create_division/',DivisionCreateView.as_view(),name='create_division'),
    # path('list_division/',DivisionListView.as_view(),name='list_division'),
    
    #test
    
    # path('list_affectation_sim/',AffectationSimListView.as_view(),name='list_affectation_sim'),
    path('ticket_Form/',TicketCreateView.as_view(),name='ticketForm'),
    path('complet/',CombinedFormView1.as_view(),name='complet'),
    # path('ticket_creat_sim/',Ticket_creat_sim.as_view(),name='ticket_creat_sim'),

]