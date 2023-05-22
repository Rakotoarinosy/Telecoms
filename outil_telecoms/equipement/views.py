from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView
from django.views.generic import ListView

from equipement.forms import ModeleForm, TypeEquipementForm
from equipement.models import Article_modele, Materiel
# Create your views here.

def equipement(request):
    return render(request,'equipement.html')

#PARAMETRAGE
##paramètrage équipement
###EQUIPEMENT
class Type_equipementCreateView(FormView):
    form_class = TypeEquipementForm
    template_name = 'Parametrage/Type_equipement/create_type_equipement.html'
    success_url = reverse_lazy('type_equipement')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
    
class Type_equipementDeleteView(DeleteView):
    model = Materiel
    template_name = 'Parametrage/Type_equipement/delete_type_equipement.html'
    success_url = reverse_lazy('type_equipement')
    
class Type_equipementUpdateView(UpdateView):
    model = Materiel
    form_class = TypeEquipementForm
    template_name = 'Parametrage/Type_equipement/update_type_equipement.html'
    success_url = reverse_lazy('type_equipement')
    
    def get_queryset(self):
        return Materiel.objects.all()

class  Type_equipementView(TemplateView):
    template_name = 'Parametrage/Type_equipement/type_equipement.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type_equipements'] = Materiel.objects.all()
        context['form'] = TypeEquipementForm()
        return context
    
###MODELE
class  ModeleCreateView(FormView):
    form_class = ModeleForm
    template_name = 'Parametrage/Modele/create_modele.html'
    success_url = reverse_lazy('modele')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
    
class  ModeleDeleteView(DeleteView):
    model = Article_modele
    template_name = 'Parametrage/Modele/delete_modele.html'
    success_url = reverse_lazy('modele')
    
class  ModeleUpdateView(UpdateView):
    model = Article_modele
    form_class = ModeleForm
    template_name = 'Parametrage/Modele/update_modele.html'
    success_url = reverse_lazy('modele')
    
    def get_queryset(self):
        return Article_modele.objects.all()

class ModeleView(TemplateView):
    template_name = 'Parametrage/Modele/modele.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modeles'] = Article_modele.objects.all()
        context['form'] = ModeleForm()
        return context