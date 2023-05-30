from unidecode import unidecode
from django import forms
from .models import *
from django import forms
from .models import *

class TypeEquipementForm(forms.ModelForm):
    code_analytique = forms.ModelChoiceField(queryset=Code_analytique.objects.all(), initial=Code_analytique.objects.get(libelle='RPE'), widget=forms.HiddenInput())
    class Meta:
        model = Materiel
        fields = "__all__"
        widgets = {
            'libelle': forms.TextInput(attrs={'class': 'form-control'}),
            'code_analytique': forms.Select(attrs={'class': 'form-select'}),
        }
    def clean_libelle(self):
        cleaned_libelle = unidecode(self.cleaned_data.get('libelle', ''))
        existing_typeEquipement = Materiel.objects.filter(libelle__iexact=cleaned_libelle).exclude(id=self.instance.id).exists()
        if existing_typeEquipement:
            raise forms.ValidationError("Ce type d'équipement existe déjà.")
        return cleaned_libelle

class ModeleForm(forms.ModelForm):   
    materiel = forms.ModelChoiceField(queryset=Materiel.objects.all(), initial=Materiel.objects.get(libelle='Smartphone'), widget=forms.Select(attrs={'class': 'form-select'}))    
    class Meta:
        model = Article_modele
        fields = "__all__"
        widgets = {
            'reference_modele': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def clean_reference_modele(self):
        cleaned_reference_modele = unidecode(self.cleaned_data.get('reference_modele', ''))  # Supprimer les accents du libellé
        existing_modele = Article_modele.objects.filter(reference_modele__iexact=cleaned_reference_modele).exclude(id=self.instance.id).exists()
        if existing_modele:
            raise forms.ValidationError("Ce type de Modèle existe déjà.")
        return cleaned_reference_modele

class BcForm(forms.ModelForm):   
    class Meta:
        model = Bc
        fields = "__all__"
        widgets = {
            'reference_bc' : forms.TextInput(attrs={'class': 'form-control'}),
            'date_bc' : forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
        }
    def clean_reference_bc(self):
        cleaned_reference_bc = unidecode(self.cleaned_data.get('reference_bc', ''))  # Supprimer les accents du libellé
        existing_bc = Bc.objects.filter(reference_bc__iexact=cleaned_reference_bc).exclude(id=self.instance.id).exists()
        if existing_bc:
            raise forms.ValidationError("Ce bon de commande existe déjà.")
        return cleaned_reference_bc
            
class StockForm(forms.ModelForm):   
    article_modele = forms.ModelChoiceField(queryset=Article_modele.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
  
    class Meta:
        model = Reception_article
        fields = "__all__"
        exclude = ['facture',]
        
        widgets = {
            'quantite' : forms.NumberInput(attrs={'class': 'form-control'}),
            'pu_ht' : forms.NumberInput(attrs={'class': 'form-control'}),
            'prix_global' : forms.NumberInput(attrs={'class': 'form-control'}),
            'facture' : forms.Select(attrs={'class': 'form-control'}),
            'bc' : forms.Select(attrs={'class': 'form-select'}),
        }
        

class BcStockForm(forms.ModelForm):
    article_modele = forms.ModelChoiceField(queryset=Article_modele.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    facture = forms.ModelChoiceField(queryset=Facture.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    #facture = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  
    class Meta:
        model = Reception_article
        fields = "__all__"
        widgets = {
            'quantite': forms.NumberInput(attrs={'class': 'form-control'}),
            'pu_ht': forms.NumberInput(attrs={'class': 'form-control'}),
            'prix_global': forms.NumberInput(attrs={'class': 'form-control'}),
            'bc': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_bc(self):
        cleaned_bc = unidecode(self.cleaned_data.get('bc', ''))
        existing_bc = Bc.objects.filter(reference_bc__iexact=cleaned_bc).exclude(id=self.instance.bc_id).exists()
        if existing_bc:
            raise forms.ValidationError("Ce bon de commande existe déjà.")
        return cleaned_bc