from unidecode import unidecode
from django import forms
from .models import *
from django import forms
from .models import *

class TypeEquipementForm(forms.ModelForm):
    code_analytique = forms.ModelChoiceField(queryset=Code_analytique.objects.all(), initial=Code_analytique.objects.get(libelle='RPE'), widget=forms.HiddenInput())    
    # code_analytique = forms.ModelChoiceField(queryset=Code_analytique.objects.all(), initial=None , widget=forms.HiddenInput())    
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
    class Meta:
        model = Article_modele
        fields = "__all__"
        widgets = {
            'reference_modele': forms.TextInput(attrs={'class': 'form-control'}),
            'materiel': forms.Select(attrs={'class': 'form-select'}),
        }
    def clean_libelle(self):
        cleaned_reference_modele = unidecode(self.cleaned_data.get('reference_modele', ''))  # Supprimer les accents du libellé
        existing_modele = Article_modele.objects.filter(libelle__iexact=cleaned_reference_modele).exclude(id=self.instance.id).exists()
        if existing_modele:
            raise forms.ValidationError("Ce type de Modèle existe déjà.")
        return cleaned_reference_modele