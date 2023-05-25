from datetime import datetime
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.http import JsonResponse
from sim.models import *

from sim.forms import AccesForm, Affectation_simFormUpdate, AffectationSimForm, CombinedCompletForm, CombinedFormTest, ForfaitForm, ForfaitFormUpdate,OperateurForm, ProfilForm, ProfilUpdateForm, SimForm, Ticket_creat_simForm,TicketForm, Type_SimForm

from django.contrib.auth import logout
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
    success_url = reverse_lazy('profil')

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
    success_url = reverse_lazy('profil')
    
class ProfilUpdateView(UpdateView):
    model = Profil
    form_class = ProfilUpdateForm
    template_name = 'Parametrage/Gestion_utilisateur/Profil/update_profil.html'
    success_url = reverse_lazy('profil')
    
    def get_queryset(self):
        return Profil.objects.all()

class ProfilView(TemplateView):
    template_name = 'Parametrage/Gestion_utilisateur/Profil/profil.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profils'] = Profil.objects.all()
        context['form'] = ProfilForm()
        return context
    
###OPERATEUR
class OperateurCreateView(FormView):
    form_class = OperateurForm
    template_name = 'Parametrage/Sim/Operateur/create_operateur.html'
    success_url = reverse_lazy('operateur')

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
    success_url = reverse_lazy('operateur')
    
class OperateurUpdateView(UpdateView):
    model = Operateur
    form_class = OperateurForm
    template_name = 'Parametrage/Sim/Operateur/update_operateur.html'
    success_url = reverse_lazy('operateur')
    
    def get_queryset(self):
        return Operateur.objects.all()

class OperateurView(TemplateView):
    template_name = 'Parametrage/Sim/Operateur/operateur.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operateurs'] = Operateur.objects.all()
        context['form'] = OperateurForm()
        return context
    
def get_operateur(request):
    operateur_id = request.GET.get('operateur_id')  # Correction : utiliser 'collaborateur_id' au lieu de 'collaborateur'
    try:
        operateur = Operateur.objects.get(id=operateur_id)  # Correction : utiliser 'id' au lieu de 'collaborateur'
        data = {
            'identifiant': operateur.identifiant,
        }
        return JsonResponse(data)
    except Collaborateur.DoesNotExist:
        return JsonResponse({'error': 'operateur introuvable'})

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

class AccesView(TemplateView):
    template_name = 'Parametrage/Sim/Acces/acces.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['access'] = Acces_sim.objects.all()
        context['form'] = AccesForm()
        return context

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

class Type_SimView(TemplateView):
    template_name = 'Parametrage/Sim/Type_sim/type_sim.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type_sims'] = Type_sim.objects.all()
        context['form'] = Type_SimForm()
        return context
    
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

class ForfaitView(TemplateView):
    template_name = 'Parametrage/Sim/Forfait/forfait.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forfaits'] = Forfait.objects.all()
        context['form'] = ForfaitForm()
        return context

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
        context['collaborateurs'] = Collaborateur.objects.all().values('id', 'nom', 'prenom')
        return context
    
# Auto complete_collaborateur_AffectationSimCreateView
def get_collaborateur(request):
    collaborateur_id = request.GET.get('collaborateur_id')  # Correction : utiliser 'collaborateur_id' au lieu de 'collaborateur'

    try:
        collaborateur = Collaborateur.objects.get(id=collaborateur_id)  # Correction : utiliser 'id' au lieu de 'collaborateur'
        data = {
            'nom': collaborateur.nom,
            'prenom': collaborateur.prenom,
        }
        return JsonResponse(data)
    except Collaborateur.DoesNotExist:
        return JsonResponse({'error': 'Collaborateur introuvable'})

    
#List_affecation   
class AffectationSimListView(ListView):
    model = Affectation_sim
    template_name = 'Sim/list_affectation_sim.html'
    context_object_name = 'affectationSims'
    
#Update_affecation   
class AffectationSimUpdateView(UpdateView):
    model = Affectation_sim
    form_class = Affectation_simFormUpdate
    template_name = 'Sim/update_list_affectation_sim.html'
    success_url = reverse_lazy('list_affectation_sim')
    
    def get_queryset(self):
        return Forfait.objects.all()
    
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
        context['forfaits'] = Forfait.objects.all().values('id', 'montantPlafondVoix', 'montantPlafondData','typeSim_id')
        return context      
    
# Auto complete_forfait_SimCreateView
def get_forfait(request):
    forfait_id = request.GET.get('forfait_id')  # Correction : utiliser 'forfait_id' au lieu de 'forfait'

    try:
        forfait = Forfait.objects.get(id=forfait_id)  # Correction : utiliser 'id' au lieu de 'forfait'
        data = {
            'montantPlafondVoix': forfait.montantPlafondVoix,
            'montantPlafondData': forfait.montantPlafondData,
            'typeSim_id': forfait.typeSim_id,
            'plafondInterne': forfait.plafondInterne,
        }
        return JsonResponse(data)
    except Forfait.DoesNotExist:
        return JsonResponse({'error': 'Forfait introuvable'})
    

class TicketCreateView(FormView):
    template_name = 'Sim/Ticket_create_sim.html'
    form_class = TicketForm
    success_url = reverse_lazy('ticketForm')  # URL de redirection en cas de succès

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class Ticket_creat_sim(FormView):
    template_name = 'Sim/Ticket_create_sim.html'
    form_class = TicketForm
    success_url = reverse_lazy('list_affectation_sim')  # URL de redirection en cas de succès

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
# class CombinedFormView1(FormView):
#     template_name = 'Sim/combined1.html'
#     form_class = CombinedCompletForm
#     success_url = reverse_lazy('list_affectation_sim')  # URL de redirection en cas de succès

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
    
class CombinedTest(FormView):
    template_name = 'Sim/combined.html'
    form_class = CombinedFormTest
    success_url = reverse_lazy('list_affectation_sim')  # URL de redirection en cas de succès

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

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

#combinaisons sim ticket mandeh
# def my_view(request):
#     model1_form = TicketForm()
#     model2_form = SimForm()

#     if request.method == 'POST':
#         model1_form = TicketForm(request.POST)
#         model2_form = SimForm(request.POST)

#         if model1_form.is_valid() and model2_form.is_valid():
#             # Enregistrer les données dans les modèles
#             model1_instance = model1_form.save()
#             model2_instance = model2_form.save()

#             # Autres opérations...

#     return render(request, 'Sim/my_template.html', {
#         'model1_form': model1_form,
#         'model2_form': model2_form,
#     })

#Mandeh fa version mbola mila alamina sy spésifiene ny champs fa misy miveina indroa
class CombinedFormView1(FormView):
    template_name = 'Sim/my_template.html'
    form_class = AffectationSimForm  # Utilisez l'un des formulaires pour initialiser la vue
    success_url = reverse_lazy('list_affectation_sim')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model1_form'] = TicketForm()
        context['model2_form'] = SimForm()
        context['model3_form'] = AffectationSimForm()
        return context

    def post(self, request, *args, **kwargs):
        model1_form = TicketForm(request.POST)
        model2_form = SimForm(request.POST)
        model3_form = AffectationSimForm(request.POST)

        if model1_form.is_valid() and model2_form.is_valid() and model3_form.is_valid():
            # Enregistrer les données dans les modèles
            model1_instance = model1_form.save()
            model2_instance = model2_form.save()
            model3_instance = model3_form.save()

            # Autres opérations...

            return self.form_valid(model1_form)  # Redirection après succès

        else:
            return self.form_invalid()

    def form_valid(self, form):
        # Logique à exécuter lorsque tous les formulaires sont valides
        # Redirection vers une page de succès, par exemple
        return super().form_valid(form)

##############################################################
def sim_view(request):
    forfaits = Forfait.objects.all()
    acces = Acces_sim.objects.all()
    etat = Etat.objects.all()
    operateur = Operateur.objects.all()
    contexte_acces = {
        "access": acces,
        # Ajoutez d'autres clés et valeurs spécifiques à AutreModele1
    }

    contexte_etat = {
        "etats": etat,
        # Ajoutez d'autres clés et valeurs spécifiques à AutreModele2
    }

    contexte_operateur = {
        "operateurs": operateur,
        # Ajoutez d'autres clés et valeurs spécifiques à AutreModele3
    }

    # Fusionnez tous les dictionnaires de contexte avec le contexte existant
    contexte_global = {
        "forfaits": forfaits,
        **contexte_acces,
        **contexte_etat,
        **contexte_operateur,
    }
       
    return render (request,'sim/affectation_siml.html', context=contexte_global)

def affect_sim(request) :
    if request.method == 'POST':
        ticket = request.POST.get('numeroTicket')
        numeros = request.POST.get('numero')

        sims = Sim.objects.filter(numero= numeros)
        if sims.exists() : 
            return render(request,'sim/affectation_siml.html')
        tickets = Ticket.objects.filter (numero_ticket = ticket)
        if not tickets.exists() : 
            compte_fact=  get_object_or_404(Compte_facturation,id= 1)
            ticket_model = Ticket.objects.create(
                numero_ticket = ticket,
                dateDemande = datetime.now(),
                dateApprobation = datetime.now(),
                compte_facturation = compte_fact
            )
        #num_tickets = Ticket.objects.filter (numero_ticket = ticket)
        Op = get_object_or_404(Operateur,id= request.POST.get('id_operateur'))
        ac = get_object_or_404(Acces_sim,id= request.POST.get('id_acces'))
        et= get_object_or_404(Etat,id= request.POST.get('id_etat'))
        forf = get_object_or_404(Forfait,id= request.POST.get('id_forfait'))
        sim_models = Sim.objects.create(
            numero = numeros,
            adresseIP = '101.101.101.101',
            operateur = Op,
            acces = ac,
            etat = et,
            forfait = forf
        )
        return render(request,'sim/affectation_siml.html')