from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views import View 
from .forms import BcStockForm
from .models import Reception_article

from equipement.forms import BcForm, ModeleForm, StockForm, TypeEquipementForm
from equipement.models import Article_modele, Bc, Materiel, Reception_article
# Create your views here.

def equipement(request):
    return render(request,'equipement.html')

#BC
class BcCreateView(FormView):
    form_class = BcForm
    template_name = 'Equipement/Bc/create_bc.html'
    success_url = reverse_lazy('bc')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
    
# class BcListView(ListView):
#     model = Bc
#     template_name = 'Equipement/Bc/bc.html'
#     context_object_name = 'operateurs'

       
class BcDeleteView(DeleteView):
    model = Bc
    template_name = 'Equipement/Bc/delete_bc.html'
    success_url = reverse_lazy('bc')
    
class BcUpdateView(UpdateView):
    model = Bc
    form_class = BcForm
    template_name = 'Equipement/Bc/update_bc.html'
    success_url = reverse_lazy('bc')
    
    def get_queryset(self):
        return Bc.objects.all()

class BcView(TemplateView):
    template_name = 'Equipement/Bc/bc.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bcs'] = Bc.objects.all()
        context['form'] = BcForm()
        return context
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
#Stock  
class Reception_articleCreateView(FormView):
    form_class = StockForm
    template_name = 'Equipement/Stock/create_stock.html'
    success_url = reverse_lazy('stock')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
    
class Reception_articleListView(ListView):
    model = Reception_article
    template_name = 'Equipement/Stock/list_stock.html'
    context_object_name = 'stocks'
    
class Reception_articleDeleteView(DeleteView):
    model = Reception_article
    template_name = 'Equipement/Stock/delete_stock.html'
    success_url = reverse_lazy('stock')
    
class Reception_articleUpdateView(UpdateView):
    model = Reception_article
    form_class = StockForm
    template_name = 'Equipement/Stock/update_stock.html'
    success_url = reverse_lazy('stock')
    
    def get_queryset(self):
        return Reception_article.objects.all()

class Reception_articleView(TemplateView):
    template_name = 'Equipement/Stock/stock.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stocks'] = Reception_article.objects.all()
        context['form'] = StockForm()
        return context
    
class CreateStockView(View):
    bc_stock_form_class = BcStockForm
    template_name = 'Equipement/Stock/votre_template.html'
    success_url = 'stock'

    def get(self, request):
        bc_stock_form = self.bc_stock_form_class()
        return render(request, self.template_name, {'bc_stock_form': bc_stock_form})

    def post(self, request):
        bc_stock_form = self.bc_stock_form_class(request.POST)
        
        if bc_stock_form.is_valid():
            bc_stock_form.save()
            return redirect(self.success_url)

        return render(request, self.template_name, {'bc_stock_form': bc_stock_form})