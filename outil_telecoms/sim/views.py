from django.shortcuts import render
from django.urls import reverse_lazy
from django.db import IntegrityError
from django.views.generic.edit import CreateView,FormView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import ListView
from sim.models import *

from sim.forms import AccesForm, AffectationSimForm, ForfaitForm, ForfaitFormUpdate,OperateurForm, ProfilForm, ProfilUpdateForm, SimForm, Type_SimForm

from django.contrib.auth import logout
from django.shortcuts import redirect
# Accueil
def logout_view(request):
    logout(request)
    return redirect('login')

def sim(request):
    return render(request, "sim.html")

def home(request):
    return render(request,"home.html")

def parametrage(request):
    return render(request,"parametrage.html")

#PARAMETRAGE
##paramètrage sim
###PROFIL
class ProfilCreateView(FormView):
    form_class = ProfilForm
    template_name = 'Parametrage/Gestion_utilisateur/Profil/create_profil.html'
    success_url = reverse_lazy('create_profil')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
    
class ProfilListView(ListView):
    model = Profil
    template_name = 'Parametrage/Gestion_utilisateur/Profil/list_profil.html'
    context_object_name = 'profils'
    
class ProfilDeleteView(DeleteView):
    model = Profil
    template_name = 'Parametrage/Gestion_utilisateur/Profil/delete_profil.html'
    success_url = reverse_lazy('create_profil')
    
class ProfilUpdateView(UpdateView):
    model = Profil
    form_class = ProfilUpdateForm
    template_name = 'Parametrage/Gestion_utilisateur/Profil/update_profil.html'
    success_url = reverse_lazy('create_profil')
    
    def get_queryset(self):
        return Profil.objects.all()
    
###OPERATEUR
class OperateurCreateView(FormView):
    form_class = OperateurForm
    template_name = 'Parametrage/Sim/Operateur/create_operateur.html'
    success_url = reverse_lazy('list_operateur')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
    
class OperateurListView(ListView):
    model = Operateur
    template_name = 'Parametrage/Sim/Operateur/list_operateur.html'
    context_object_name = 'operateurs'
       
class OperateurDeleteView(DeleteView):
    model = Operateur
    template_name = 'Parametrage/Sim/Operateur/delete_operateur.html'
    success_url = reverse_lazy('list_operateur')
    
class OperateurUpdateView(UpdateView):
    model = Operateur
    form_class = OperateurForm
    template_name = 'Parametrage/Sim/Operateur/update_operateur.html'
    success_url = reverse_lazy('list_operateur')
    
    def get_queryset(self):
        return Operateur.objects.all()

###ACCESS
class AccesCreateView(FormView):
    form_class = AccesForm
    template_name = 'Parametrage/Sim/Acces/create_acces.html'
    success_url = reverse_lazy('list_acces')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
    
class AccesListView(ListView):
    model = Acces_sim
    template_name = 'Parametrage/Sim/Acces/list_acces.html'
    context_object_name = 'access'
    
class AccesDeleteView(DeleteView):
    model = Acces_sim
    template_name = 'Parametrage/Sim/Acces/delete_acces.html'
    success_url = reverse_lazy('list_acces')
    
class AccesUpdateView(UpdateView):
    model = Acces_sim
    form_class = AccesForm
    template_name = 'Parametrage/Sim/Acces/update_acces.html'
    success_url = reverse_lazy('list_acces')
    
    def get_queryset(self):
        return Acces_sim.objects.all()

###TYPE_SIM
class Type_SimCreateView(FormView):
    form_class = Type_SimForm
    template_name = 'Parametrage/Sim/Type_Sim/create_type_sim.html'
    success_url = reverse_lazy('list_type_sim')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
    
class Type_SimListView(ListView):
    model = Type_sim
    template_name = 'Parametrage/Sim/Type_Sim/list_type_sim.html'
    context_object_name = 'type_sims'

class Type_SimDeleteView(DeleteView):
    model = Type_sim
    template_name = 'Parametrage/Sim/Type_Sim/delete_type_sim.html'
    success_url = reverse_lazy('list_type_sim')
    
class Type_SimUpdateView(UpdateView):
    model = Type_sim
    form_class = Type_SimForm
    template_name = 'Parametrage/Sim/Type_Sim/update_type_sim.html'
    success_url = reverse_lazy('list_type_sim')
    
    def get_queryset(self):
        return Type_sim.objects.all()
    
###FORFAIT
class ForfaitCreateView(FormView):
    form_class = ForfaitForm
    template_name = 'Parametrage/Sim/Forfait/create_forfait.html'
    success_url = reverse_lazy('list_forfait')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
    
class ForfaitListView(ListView):
    model = Forfait
    template_name = 'Parametrage/Sim/Forfait/list_forfait.html'
    context_object_name = 'forfaits'
       
class ForfaitDeleteView(DeleteView):
    model = Forfait
    template_name = 'Parametrage/Sim/Forfait/delete_forfait.html'
    success_url = reverse_lazy('list_forfait')
    
class ForfaitUpdateView(UpdateView):
    model = Forfait
    form_class = ForfaitFormUpdate
    template_name = 'Parametrage/Sim/Forfait/update_forfait.html'
    success_url = reverse_lazy('list_forfait')
    
    def get_queryset(self):
        return Forfait.objects.all()

#SIM
##Affectation SIM
class AffectationSimCreateView(FormView):
    form_class = AffectationSimForm
    template_name = 'Sim/create_affectation_sim.html'
    success_url = reverse_lazy('list_affectation_sim')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
    
class AffectationSimListView(ListView):
    model = Affectation_sim
    template_name = 'Sim/list_affectation_sim.html'
    context_object_name = 'affectationSims'
    
class SimCreateView(FormView):
    form_class = SimForm
    template_name = 'Sim/create_sim.html'
    success_url = reverse_lazy('list_affectation_sim')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context        
    
#Division
# class DivisionCreateView(CreateView):
#     model = Division
#     template_name = "Division/create_division.html"
#     fields = ["libelle"]
#     success_url = reverse_lazy('list_division')    

# class DivisionListView(ListView):
#     model = Division
#     fields = "libelle"
#     template_name = "Division/list_division.html"
#     context_object_name = 'divisions'

# class DivisionDeleteView(DeleteView):
#     model = Forfait
#     template_name = 'Parametrage/Sim/Forfait/delete_division.html'
#     success_url = reverse_lazy('forfait_create_and_list')
    
# class DivisionUpdateView(UpdateView):
#     model = Forfait
#     form_class = ForfaitForm
#     template_name = 'Parametrage/Sim/Forfait/update_division.html'
#     success_url = reverse_lazy('forfait_create')
    
#     def get_queryset(self):
#         return Forfait.objects.all()
    
#TEST