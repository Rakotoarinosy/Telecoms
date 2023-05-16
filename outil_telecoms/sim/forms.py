from cProfile import Profile
from dataclasses import fields
from multiprocessing import context
from os import access
from pyexpat import model
from django import forms
from .models import *


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
        existing_profil = Profil.objects.filter(libelle__iexact=cleaned_libelle).exists()
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
        existing_profil = Profil.objects.filter(libelle__iexact=cleaned_libelle).exists()
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
        if Operateur.objects.filter(identifiant=identifiant).exists():
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
        existing_acces_sim = Acces_sim.objects.filter(libelle__iexact=cleaned_libelle).exists()
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
        existing_type_sim = Type_sim.objects.filter(libelle__iexact=cleaned_libelle).exists()
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
        existing_forfait = Forfait.objects.filter(libelle__iexact=cleaned_libelle).exists()
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
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and instance.forfait:
            self.fields['forfait'].queryset = Forfait.objects.filter(id=instance.forfait.id)
            self.fields['forfait'].initial = instance.forfait.id
            self.fields['montantPlafondVoix'] = forms.IntegerField(initial=instance.forfait.montantPlafondVoix, required=False)
            self.fields['montantPlafondData'] = forms.IntegerField(initial=instance.forfait.montantPlafondData, required=False)
        else:
            self.fields['montantPlafondVoix'] = forms.IntegerField(required=False)
            self.fields['montantPlafondData'] = forms.IntegerField(required=False)
            
            
class AffectationSimForm(forms.ModelForm):

    class Meta:
        model = Affectation_sim
        fields = "__all__"
        widgets = {
            'ticket': forms.NumberInput(attrs={'class': 'form-control'}),
            'sim': forms.TextInput(attrs={'class': 'form-control'}),
            'collaborateur': forms.TextInput(attrs={'class': 'form-control'}),
        }      
        

        