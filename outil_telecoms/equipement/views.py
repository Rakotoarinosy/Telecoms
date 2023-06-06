from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views import View
import json
from django.contrib import messages
from sim.models import Collaborateur, Compte_facturation, Etat, Ticket 
from .forms import AffectationArticleForm, BcStockForm
from .models import Affectation_article, Article, Facture, Reception_article, Sortie, Mouvement

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
#     context_object_name = 'articleerateurs'

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
    
def stock_equipement_view(request):
    bc = Bc.objects.all()
    article = Article_modele.objects.all()
    context = {
        "bcs": bc,
        "articles": article,
    }
    return render(request, 'Equipement/Stock/stock_equipement.html', context=context)

def affect_stock_equipement_view(request):
    bc = Bc.objects.all()
    article = Article_modele.objects.all()
    result = Mouvement.objects.filter(disponible__gt=0).values_list('article_modele_id', flat=True)
    print(result)
    resultat=Article_modele.objects.filter(id__in=result)
    print(resultat)

    if request.method == 'POST':
        ticket = request.POST.get('numeroTicket')
        dateDemande = request.POST.get('dateDemande')
        dateApprobation = request.POST.get('dateApprobation')
        collabo = request.POST.get('matricule')
        imei_1 = request.POST.get('imei_1')
        imei_2 = request.POST.get('imei_2')
        imei_3 = request.POST.get('imei_3')
        imei_4 = request.POST.get('imei_4')
        quantiteSortie = int(request.POST.get('quantite'))
        numBonSortie = request.POST.get('num_bon_sortie')
        numSortie = request.POST.get('num_sortie')
        fact = request.POST.get('id_fact')

        tickets = Ticket.objects.filter(numero_ticket=ticket)
        if not tickets.exists():
            compte_fact = get_object_or_404(Compte_facturation, id=1)
            ticket_model = Ticket.objects.create(
                numero_ticket=ticket,
                dateDemande=dateDemande,
                dateApprobation=dateApprobation,
                compte_facturation=compte_fact,
            )

        eta = get_object_or_404(Etat, id=1)
        num_tickets = Ticket.objects.filter(numero_ticket=ticket)
        article_affect = get_object_or_404(Article_modele, id=request.POST.get('id_articleReference'))
        article_ = Article.objects.create(
            imei1=imei_1,
            etat=eta,
            article_modele=article_affect,
        )

        if imei_2:
            article_.imei2 = imei_2
        if imei_3:
            article_.imei3 = imei_3
        if imei_4:
            article_.imei4 = imei_4

        article_.save()

        id_fact = Facture.objects.filter(num_facture=fact).values_list('id', flat=True)
        reception_article = Reception_article.objects.get(id=id_fact[0])
        quantite_totale = reception_article.quantite
        
        # Article_modele.objects.filter(id__in=Subquery( Mouvement.objects.filter(disponible__gt=0).values('article_modele_id')))
        
        mouvement, created = Mouvement.objects.get_or_create(article_modele=article_affect)
        mouvement.affecte += 1

        mouvement.disponible -= 1
        mouvement.save()
        # dispo = mouvement.disponible
        # print(dispo)

        # if dispo <= 0:
        #     return render(request, 'Equipement/Affectation/affectation_equipement.html', context={'message': 'stock epuisé', 'articles': article})
        # else:
        #     
        sortie_ = Sortie.objects.create(
            quantiteSortie=quantiteSortie,
            numBonSortie=numBonSortie,
            numSortie=numSortie,
            reception_article=reception_article,
        )

        collaborateur = Collaborateur.objects.get(matricule=collabo)
        if collaborateur:
            affectation_equipement = Affectation_article.objects.create(
                collaborateur=collaborateur,
                ticket=num_tickets.first(),
                article=article_,
                sortie=sortie_,
            )
            return redirect('affectation_list')

    return render(request, 'Equipement/Affectation/affectation_equipement.html', {'articles': resultat})


def affectation_update_view(request, affectation_id):
    # Récupérez l'affectationEquipement à mettre à jour depuis la base de données
    try:
        affectationEquipement = Affectation_article.objects.get(id=affectation_id)
    except Affectation_article.DoesNotExist:
        return JsonResponse({'message': 'L\'affectationEquipement n\'existe pas.'}, status=404)
    
    # Vérifiez si la méthode de requête est PUT ou PATCH
    if request.method == 'PUT' or request.method == 'PATCH':
        # Mettez à jour les attributs de l'affectationEquipement avec les nouvelles valeurs
        affectationEquipement.collaborateur = request.POST.get('nouvelle_valeur_collabo')
        # Mettez à jour d'autres attributs si nécessaire
        
        # Enregistrez les modifications dans la base de données
        affectationEquipement.save()
        
        # Retournez une réponse JSON ou une redirection appropriée
        return JsonResponse({'message': 'affectationEquipement mis à jour avec succès.'})
    
    # Retournez la réponse HTML pour la vue de mise à jour
    return render(request, 'Equipement/Affectation/affectation_edit.html', {'affectationEquipement': affectationEquipement})


class AffectationListView(ListView):
    model = Affectation_article
    template_name = 'Equipement/Affectation/list_affectation_equipement.html'
    context_object_name = 'affectationEquipements'


class AffectationArticleUpdateView(UpdateView):
    model = Affectation_article
    template_name = 'Equipement/Affectation/affectation_edit.html'
    form_class = AffectationArticleForm
    
    def get_object(self, queryset=None):
        return Affectation_article.objects.get(pk=self.kwargs['pk'])

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.instance = self.object  # Passez l'instance à votre formulaire
        return form

    def get_success_url(self):
        return 'affectationEquipements'

    
def update_stock_equipement_view(request, id_affectation):
    affectation = get_object_or_404(Affectation_article, id=id_affectation)
    bc = Bc.objects.all()
    article = Article_modele.objects.all()

    if request.method == 'POST':
        ticket = request.POST.get('numeroTicket')
        dateDemande = request.POST.get('dateDemande')
        dateApprobation = request.POST.get('dateApprobation')
        collabo = request.POST.get('matricule')
        imei_1 = request.POST.get('imei_1')
        imei_2 = request.POST.get('imei_2')
        imei_3 = request.POST.get('imei_3')
        imei_4 = request.POST.get('imei_4')
        quantiteSortie = request.POST.get('quantite')
        numBonSortie = request.POST.get('num_bon_sortie')
        numSortie = request.POST.get('num_sortie')
        fact = request.POST.get('id_fact')
        tickets = Ticket.objects.filter(numero_ticket=ticket)
        if not tickets.exists():
            compte_fact = get_object_or_404(Compte_facturation, id=1)
            ticket_model = Ticket.objects.create(
                numero_ticket=ticket,
                dateDemande=dateDemande,
                dateApprobation=dateApprobation,
                compte_facturation=compte_fact,
            )
        eta = get_object_or_404(Etat, id=1)
        num_tickets = Ticket.objects.filter(numero_ticket=ticket)
        article_affect = get_object_or_404(Article_modele, id=request.POST.get('id_articleReference'))
        article_ = Article.objects.create(
            imei1 = imei_1,
            imei2 = imei_2,
            imei3 = imei_3,
            imei4 = imei_4,
            etat = eta,
            article_modele = article_affect,
        )
        id_fact = Facture.objects.filter(num_facture=fact).values_list('id', flat=True)
        reception_article = Reception_article.objects.filter(id=id_fact[0]).first()
        sortie_ = Sortie.objects.create(
            quantiteSortie = quantiteSortie,
            numBonSortie = numBonSortie,
            numSortie = numSortie,
            reception_article = reception_article,
        )   
        collaborateur = Collaborateur.objects.get(matricule=collabo)
        if collaborateur:
            affectation_equipement = Affectation_article.objects.create(
                collaborateur = collaborateur,
                ticket=num_tickets.first(),
                article = article_,
                sortie = sortie_,
            )

        return redirect('list_affectation_sims')

    return render(request, 'Equipement/Affectation/affectation_edit.html', {'affectation': affectation, 'articles': article})


def reception_stock_equipement_view(request):
    articles = Article_modele.objects.all()
    if request.method == 'POST':
        qt = request.POST.get('id_quantite')
        pg = request.POST.get('id_prixglobal')
        pu = request.POST.get('id_pu_ht')
        facture = request.POST.get('numeroFacture')
        dateFacture = request.POST.get('dateFacture')
        bc = request.POST.get('ref_bc')
        dateBc = request.POST.get('dateBc')
        facture_ = Facture.objects.filter(num_facture=facture).first()
        if not facture_:
            facture_ = Facture.objects.create(
                num_facture=facture,
                dateFacture=dateFacture,
            )
        bc_ = Bc.objects.filter(reference_bc=bc).first()
        if not bc_:
            bc_ = Bc.objects.create(
                reference_bc=bc,
                date_bc=dateBc,
            )
        reference = get_object_or_404(Article_modele, id=request.POST.get('id_articleReference'))
        reception = Reception_article.objects.create(
            quantite=qt,
            prix_global=pg,
            pu_ht=pu,
            bc=bc_,
            facture=facture_,
            article_modele=reference,
        )
        #filtrer mouvement si article_modele = reference
        #si n'existe pas => create mouvement 
        #disponible = qt
        #si existe =>update mouvement
        #disponible = disponible + qte
        mouvement = Mouvement.objects.all()
        
        exist = Mouvement.objects.filter(article_modele=reference)
        if not exist:
            exist = Mouvement.objects.create(
                disponible = qt,
                article_modele = reference,
            )
        else:
            exist = exist.first()  # Sélectionner le premier objet de la requête existante
            exist.disponible += int(qt)  # Ajouter qte à la valeur existante de disponible
            exist.save()  # Enregistrer les modifications dans la base de données
            
        return redirect('affectation_list')
    return render(request, 'Equipement/Reception/stock_equipement.html', {'articles': articles})

def get_materiel(request):
    article_id = request.GET.get('article_id')
    try:
        reference = Article_modele.objects.get(id=article_id)
        materiel = Materiel.objects.get(id=reference.materiel_id)

        data = {
            'materiel': str(materiel.libelle),
        }
        return JsonResponse(data)
    except Article_modele.DoesNotExist:
        return JsonResponse({'error': 'Article introuvable'})
    
def autocomplete_bc(request):
    num_facture = request.GET.get("num_facture", "")
    try:
        reception_articles = Reception_article.objects.filter(facture__num_facture__istartswith=num_facture)
        data = [{"num_facture": reception_article.facture.num_facture, "bc": reception_article.bc.reference_bc} for reception_article in reception_articles]
    except (Facture.DoesNotExist, Reception_article.DoesNotExist):
        data = []

    return JsonResponse(data, safe=False)