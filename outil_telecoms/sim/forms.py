from cProfile import Profile
from dataclasses import fields
from multiprocessing import context
from os import access
from pyexpat import model
from urllib import request
from django import forms
from .models import *
from unidecode import unidecode
from django.shortcuts import render,redirect

class ProfilForm(forms.ModelForm):
    etat = forms.ModelChoiceField(queryset=Etat.objects.all(), initial=Etat.objects.get(libelle='Actif'), widget=forms.HiddenInput())    
    class Meta:
        model = Profil
        fields = ("libelle","etat")
        widgets = {
            'libelle': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def clean_libelle(self):
        cleaned_libelle = unidecode(self.cleaned_data.get('libelle', ''))  # Supprimer les accents du libellé
        existing_profil = Profil.objects.filter(libelle__iexact=cleaned_libelle).exclude(id=self.instance.id).exists()
        if existing_profil:
            raise forms.ValidationError("Ce type de profil existe déjà.")
        return cleaned_libelle
    
class ProfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = "__all__"
        widgets = {
            'libelle': forms.TextInput(attrs={'class': 'form-control'}),
            'etat': forms.Select(attrs={'class': 'form-select'}),
        }
    def clean_libelle(self):
        cleaned_libelle = unidecode(self.cleaned_data.get('libelle', ''))  # Supprimer les accents du libellé
        existing_profil = Profil.objects.filter(libelle__iexact=cleaned_libelle).exclude(id=self.instance.id).exists()
        if existing_profil:
            raise forms.ValidationError("Ce type de profil existe déjà.")
        return cleaned_libelle
    
        
class OperateurForm(forms.ModelForm):
    class Meta:
        model = Operateur
        fields = "__all__"
        widgets = {
            'libelle': forms.TextInput(attrs={'class': 'form-control'}),
            'identifiant': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    def clean_identifiant(self):
        identifiant = self.cleaned_data.get('identifiant') 
        # Vérifier si l'identifiant existe déjà
        if Operateur.objects.filter(identifiant=identifiant).exclude(id=self.instance.id).exists(): 
            raise ValidationError("Cet identifiant existe déjà.")

        return identifiant
        
class AccesForm(forms.ModelForm):
    class Meta:
        model = Acces_sim
        fields = "__all__"
        widgets = {
            'libelle': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def clean_libelle(self):
        cleaned_libelle = unidecode(self.cleaned_data.get('libelle', ''))  # Supprimer les accents du libellé
        existing_acces_sim = Acces_sim.objects.filter(libelle__iexact=cleaned_libelle).exclude(id=self.instance.id).exists()
        if existing_acces_sim:
            raise forms.ValidationError("Ce type d'accès' existe déjà.")
        return cleaned_libelle        
        
class Type_SimForm(forms.ModelForm):
    class Meta:
        model = Type_sim
        fields = "__all__"
        widgets = {
            'libelle': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
    def clean_libelle(self):
        cleaned_libelle = unidecode(self.cleaned_data.get('libelle', ''))  # Supprimer les accents du libellé
        existing_type_sim = Type_sim.objects.filter(libelle__iexact=cleaned_libelle).exclude(id=self.instance.id).exists()
        if existing_type_sim:
            raise forms.ValidationError("Ce type de SIM existe déjà.")
        return cleaned_libelle
        
class ForfaitForm(forms.ModelForm):
    class Meta:
        model = Forfait
        fields = "__all__"
        widgets = {
            'libelle': forms.TextInput(attrs={'class': 'form-control'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control'}),
            'montantPlafondVoix': forms.NumberInput(attrs={'class': 'form-control', 'style': 'display: none;'}),
            'montantPlafondData': forms.NumberInput(attrs={'class': 'form-control', 'style': 'display: none;'}),
            'plafondInterne': forms.NumberInput(attrs={'class': 'form-control'}),
            'typeSim': forms.Select(attrs={'class': 'form-select', 'onchange': 'updateChampsAffiches();'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(ForfaitForm, self).__init__(*args, **kwargs)
        self.fields['montantPlafondVoix'].initial = 0
        self.fields['montantPlafondData'].initial = 0
        
    def clean_libelle(self):
        cleaned_libelle = unidecode(self.cleaned_data.get('libelle', ''))  # Supprimer les accents du libellé
        existing_forfait = Forfait.objects.filter(libelle__iexact=cleaned_libelle).exclude(id=self.instance.id).exists()
        if existing_forfait:
            raise forms.ValidationError("Ce type de forfait existe déjà.")
        return cleaned_libelle
    
class ForfaitFormUpdate(forms.ModelForm):
    class Meta:
        model = Forfait
        fields = "__all__"
        widgets = {
            'libelle': forms.TextInput(attrs={'class': 'form-control'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control'}),
            'montantPlafondVoix': forms.NumberInput(attrs={'class': 'form-control'}),
            'montantPlafondData': forms.NumberInput(attrs={'class': 'form-control'}),
            'plafondInterne': forms.NumberInput(attrs={'class': 'form-control'}),
            'typeSim': forms.Select(attrs={'class': 'form-select', 'onchange': 'updateChampsAffiches();'}),
        }
        
    def clean_libelle(self):
        cleaned_libelle = unidecode(self.cleaned_data.get('libelle', ''))
        existing_forfait = Forfait.objects.filter(libelle__iexact=cleaned_libelle).exclude(id=self.instance.id).exists()
        if existing_forfait:
            raise forms.ValidationError("Ce type de forfait existe déjà.")
        return cleaned_libelle
    
class SimForm(forms.ModelForm):
    forfait = forms.ModelChoiceField(queryset=Forfait.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Sim
        fields = "__all__"
        widgets = {
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'adresseIP': forms.TextInput(attrs={'class': 'form-control'}),
            'typeSim': forms.Select(attrs={'class': 'form-control'}),
            'acces': forms.Select(attrs={'class': 'form-control'}),
            'operateur': forms.Select(attrs={'class': 'form-control'}),
            'etat': forms.Select(attrs={'class': 'form-control'}),
        }
    def clean_numero(self):
        numero = self.cleaned_data.get('numero') 
        # Vérifier si l'identifiant existe déjà
        if Sim.objects.filter(numero=numero).exclude(id=self.instance.id).exists(): 
            raise ValidationError("Ce numéro existe déjà.") 
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and instance.forfait:
            self.fields['forfait'].queryset = Forfait.objects.filter(id=instance.forfait.id)
            self.fields['forfait'].initial = instance.forfait.id
            self.fields['montantPlafondVoix'] = forms.IntegerField(initial=instance.forfait.montantPlafondVoix, required=False,widget=forms.NumberInput(attrs={'class':'form-control','disabled': 'disabled',}))
            self.fields['montantPlafondData'] = forms.IntegerField(initial=instance.forfait.montantPlafondData, required=False,widget=forms.NumberInput(attrs={'class':'form-control','disabled': 'disabled',}))
            self.fields['typeSim_id'] = forms.CharField(initial=instance.forfait.typeSim_id, required=False,widget=forms.NumberInput(attrs={'class':'form-control','disabled': 'disabled',}))
        else:
            self.fields['montantPlafondVoix'] = forms.IntegerField(required=False,widget=forms.NumberInput(attrs={'class':'form-control','disabled': 'disabled',}))
            self.fields['montantPlafondData'] = forms.IntegerField(required=False,widget=forms.NumberInput(attrs={'class':'form-control','disabled': 'disabled'}))
            self.fields['typeSim_id'] = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','disabled': 'disabled'}))
        
        self.fields['montantPlafondVoix'].label = "Montant Plafond Voix"
        self.fields['montantPlafondData'].label = "Montant Plafond Data"
        self.fields['typeSim_id'].label = "Type de SIM "

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"
        widgets = {
            'numero_ticket': forms.TextInput(attrs={'class': 'form-control'}),
            'dateDemande': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'dateApprobation': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'compte_facturation': forms.Select(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['numero_ticket'].label = "Numéro Ticket"
       
class AffectationSimForm(forms.ModelForm):
    collaborateur = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'matricule', 'name': 'matricule'}))

    class Meta:
        model = Affectation_sim
        fields = "__all__"
        exclude = ["ticket", "sim", "dateModification", "dateDesactivation"]
        widgets = {
            'ticket': forms.Select(attrs={'class': 'form-control'}),
            'sim': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and instance.forfait:
            self.fields['collaborateur'].initial = instance.collaborateur.nom
        self.fields['nom'] = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'disabled': 'disabled'}))
        self.fields['prenom'] = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'disabled': 'disabled'}))

class Affectation_simFormUpdate(forms.ModelForm):
    class Meta:
        model = Affectation_sim
        fields = "__all__"
        widgets = {
            'dateDesactivation': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'dateModification': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'libelle': forms.TextInput(attrs={'class': 'form-control'}),
            'collaborateur': forms.Select(attrs={'class': 'form-select'}),
            'ticket': forms.Select(attrs={'class': 'form-control'}),
            'sim': forms.Select(attrs={'class': 'form-control'}),
        }
        
class CombinedCompletForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields.update(TicketForm().fields)
        self.fields.update(SimForm().fields)
        self.fields.update(AffectationSimForm().fields)

    def clean(self):
        cleaned_data = super().clean()
        # Ajoutez ici votre logique de validation personnalisée si nécessaire
        return cleaned_data

    # def save(self):
    #     # Ajoutez ici votre logique d'enregistrement personnalisée si nécessaire
    #     pass   
    
    # def save(self):
    #     ticket_data = self.cleaned_data.get('ticket')
    #     sim_data = self.cleaned_data.get('sim')
    #     affectation_sim_data = self.cleaned_data.get('affectation_sim')

    #     # Créer l'objet Ticket avec les données de ticket_data
    #     ticket = Ticket.objects.create(**ticket_data)

    #     # Créer l'objet Sim avec les données de sim_data
    #     sim = Sim.objects.create(**sim_data)

    #     # Créer l'objet Affectation_sim avec les données de affectation_sim_data
    #     affectation_sim = Affectation_sim.objects.create(**affectation_sim_data)

    #     # Effectuer les associations ForeignKey nécessaires
    #     affectation_sim.ticket = ticket
    #     affectation_sim.sim = sim
    #     affectation_sim.save()
    
    def save(self):
        ticket_data = self.cleaned_data.get('ticket')
        sim_data = self.cleaned_data.get('sim')
        affectation_sim_data = self.cleaned_data.get('affectation_sim')

        # Créez l'objet Ticket avec les données de ticket_data
        ticket = Ticket.objects.create(**ticket_data)

        # Créez l'objet Sim avec les données de sim_data
        sim = Sim.objects.create(**sim_data)

        # Créez l'objet Affectation_sim avec les données de affectation_sim_data
        affectation_sim = Affectation_sim.objects.create(**affectation_sim_data)

        # Effectuez les associations ForeignKey nécessaires
        affectation_sim.ticket = ticket
        affectation_sim.sim = sim
        affectation_sim.save()
        
        form = CombinedCompletForm(request.POST)
        if form.is_valid():
            form.save()
            # Autres actions à effectuer en cas de succès
        else:
            # Gérer les erreurs de validation du formulaire
            return ('erreue d\'envoi')



class Ticket_creat_simForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields.update(TicketForm().fields)
        self.fields.update(SimForm().fields)
    def clean(self):
        cleaned_data = super().clean()
        # Ajoutez ici votre logique de validation personnalisée si nécessaire
        return cleaned_data
    
    def save(self):
        ticket_data = self.cleaned_data.get('ticket')
        sim_data = self.cleaned_data.get('sim')

        # Créer l'objet Ticket avec les données de ticket_data
        ticket = Ticket.objects.create(**ticket_data)

        # Créer l'objet Sim avec les données de sim_data
        sim = Sim.objects.create(**sim_data)
    
# class CombinedForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         self.fields.update(SimForm().fields)
#         self.fields.update(AffectationSimForm().fields)

#     def clean(self):
#         cleaned_data = super().clean()
#         # Ajoutez ici votre logique de validation personnalisée si nécessaire
#         return cleaned_data

#     def save(self):
#         ticket_data = self.cleaned_data.get('ticket')
#         sim_data = self.cleaned_data.get('sim')

#         # Créez les objets Ticket, Sim et Affectation_sim avec les données du formulaire
#         ticket = Ticket.objects.create(**ticket_data)
#         sim = Sim.objects.create(**sim_data)

#         # Effectuez les associations ForeignKey nécessaires
#         sim.ticket = ticket
#         sim.save()


class CombinedFormTest(forms.ModelForm):
    numero = forms.IntegerField(label="Numéro Téléphone", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    adresseIP = forms.CharField(label="Adresse IP", widget=forms.TextInput(attrs={'class': 'form-control'}))
    operateur = forms.ModelChoiceField(queryset=Operateur.objects.all(), label="Opérateur", widget=forms.Select(attrs={'class': 'form-control'}))
    acces = forms.ModelChoiceField(queryset=Acces_sim.objects.all(), label="Accès", widget=forms.Select(attrs={'class': 'form-control'}))
    etat = forms.ModelChoiceField(queryset=Etat.objects.all(), label="Etat", widget=forms.Select(attrs={'class': 'form-control'}))
    forfait = forms.ModelChoiceField(queryset=Forfait.objects.all(), label="Forfait", widget=forms.Select(attrs={'class': 'form-control'}))
    dateDemande = forms.DateField(label="Date de demande", widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    dateApprobation = forms.DateField(label="Date d'approbation", widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    compte_facturation = forms.ModelChoiceField(queryset=Compte_facturation.objects.all(), label="Compte de Facturation", widget=forms.Select(attrs={'class': 'form-control'}))
    numero_ticket = forms.CharField(label="Numéro Ticket", widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Sim
        fields = ['numero', 'adresseIP', 'operateur', 'acces', 'etat', 'forfait', 'numero_ticket' ,'dateDemande', 'dateApprobation', 'compte_facturation']

    def save_combined_form(request):
        if request.method == 'POST':
            form = CombinedFormTest(request.POST)
            if form.is_valid():
                sim = form.save(commit=False)  # Obtient une instance de Sim à partir du formulaire sans enregistrer immédiatement
                ticket = Ticket()  # Instancie un nouvel objet Ticket
                
                # Récupère les données du formulaire
                numero_ticket = form.cleaned_data['numero_ticket']
                
                # Associe les valeurs aux champs du modèle Ticket
                ticket.numero = numero_ticket
                # Associez d'autres valeurs de champs de Ticket si nécessaire
                
                # Enregistre les instances de Sim et Ticket dans la base de données
                sim.save()
                ticket.save()
                
                # Effectue d'autres actions nécessaires ou redirige vers une autre page
                
                return redirect('nom_de_la_vue')  # Redirection vers une autre vue après la sauvegarde
        else:
            form = CombinedFormTest()
        
        context = {
            'form': form
        }
        
        return render(request, 'template.html', context)
    
    
