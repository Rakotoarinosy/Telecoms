from django.core.exceptions import ValidationError
from django.db import models
# from django.db.models.signals import pre_save
# from django.dispatch import receiver
from django.db.models.functions import Lower
from unidecode import unidecode

# Create your models here.
class Compte_facturation(models.Model):
    libelle = models.CharField(max_length=40,verbose_name="Compte de facturation",)
    def __str__(self):
        return self.libelle

class Ticket(models.Model):
    numero_ticket = models.CharField(max_length=50,verbose_name="Numéro ticket",)
    dateDemande = models.DateField(verbose_name="Date de demande")
    dateApprobation = models.DateField(verbose_name="Date d'approbation")
    compte_facturation = models.ForeignKey(Compte_facturation,on_delete=models.SET_NULL, null=True,verbose_name="Compte de Facturation")

    def __str__(self):
        return str(self.numero_ticket)
    
class Division(models.Model):
    libelle = models.CharField(max_length=10,verbose_name="Division",)
    
    def __str__(self):
        return self.libelle

class Departement(models.Model):
    libelle = models.CharField(max_length=40,verbose_name="Département",)
    
    def __str__(self):
        return self.libelle

class Site(models.Model):
    libelle = models.CharField(max_length=40,verbose_name="Site",)
    
    def __str__(self):
        return self.libelle

class Etat(models.Model):
    libelle = models.CharField(verbose_name="Etat",max_length=30,default="Actif")
    
    def __str__(self):
        return self.libelle

class Service(models.Model):
    libelle = models.CharField(max_length=40,verbose_name="Service",)
    
    def __str__(self):
        return self.libelle
    
class Classe(models.Model):
    libelle = models.CharField(max_length=40,verbose_name="Classe",)
    
    def __str__(self):
        return self.libelle

class Profil(models.Model):
    libelle = models.CharField(max_length=40,verbose_name="Profil",)
    etat = models.ForeignKey(Etat,on_delete=models.SET_NULL,null=True,verbose_name="Etat")
        
    def __str__(self):
        return str(self.libelle)

class Collaborateur(models.Model):
    matricule = models.CharField(unique=True,verbose_name="Matricule")
    nom = models.CharField(max_length=150,verbose_name="Nom")
    prenom = models.CharField(max_length=150,verbose_name="Prénoms")
    fonction = models.CharField(max_length=150,verbose_name="Fonction")
    division = models.ForeignKey(Division,on_delete=models.SET_NULL, null=True,verbose_name="Division")
    departement = models.ForeignKey(Departement,on_delete=models.SET_NULL, null=True,verbose_name="Département")
    site = models.ForeignKey(Site,on_delete=models.SET_NULL, null=True,verbose_name="Site")
    service = models.ForeignKey(Service,on_delete=models.SET_NULL, null=True,verbose_name="Service")
    classe = models.ForeignKey(Classe,on_delete=models.SET_NULL, null=True,verbose_name="Classe")
    
    def __str__(self):
        return self.matricule
    
class Operateur(models.Model):
    identifiant = models.IntegerField(verbose_name="Identifiant")
    libelle = models.CharField(max_length=20,verbose_name="Opérateur")
    
    def __str__(self):
        return self.libelle

class Acces_sim(models.Model):
    libelle = models.CharField(max_length=20,verbose_name="Accès")
    
    def __str__(self):
        return self.libelle

class Type_sim(models.Model):
    libelle = models.CharField(max_length=20, unique=True, verbose_name="Type de SIM")

    def __str__(self):
        return self.libelle

class Forfait(models.Model):
    libelle = models.CharField(max_length=20,verbose_name="Forfait")
    typeSim = models.ForeignKey(Type_sim,on_delete=models.SET_NULL,null=True,verbose_name="Type de SIM")
    montant = models.IntegerField(verbose_name="Montant")
    montantPlafondVoix = models.IntegerField(verbose_name="Montant Plafond Voix",blank=True,null=True)
    montantPlafondData = models.IntegerField(verbose_name="Montant Plafond Data",blank=True,null=True)
    plafondInterne = models.IntegerField(verbose_name="Plafond Interne")
    
    def __str__(self):
        return self.libelle
        
class Sim(models.Model):
    numero = models.IntegerField(verbose_name="Numéro Téléphone")
    adresseIP = models.CharField(verbose_name="Adresse IP",blank=True,null=True)
    operateur = models.ForeignKey(Operateur,on_delete=models.SET_NULL,null=True,verbose_name="Opérateur")
    acces = models.ForeignKey(Acces_sim,on_delete=models.SET_NULL,null=True,verbose_name="Accès")
    etat = models.ForeignKey(Etat,on_delete=models.SET_NULL,null=True,verbose_name="Etat")
    forfait = models.ForeignKey(Forfait,on_delete=models.SET_NULL,null=True,verbose_name="Forfait")
    
    def __str__(self):
         return str(self.numero)

class Affectation_sim(models.Model):
    dateAffectation = models.DateField(auto_now=True,verbose_name="Date d'affectation")
    dateActivation = models.DateField(auto_now=True,verbose_name="Date d'activation")
    dateDesactivation = models.DateField(verbose_name="Date de désactivation",blank=True,null=True)
    dateModification = models.DateField(verbose_name="Date de modification",blank=True,null=True)
    ticket = models.ForeignKey(Ticket,on_delete=models.SET_NULL,null=True,verbose_name="Numéro Ticket")
    sim = models.ForeignKey(Sim,on_delete=models.SET_NULL,null=True,verbose_name="Numéro")
    collaborateur = models.ForeignKey(Collaborateur,on_delete=models.SET_NULL,null=True,verbose_name="Collaborateur")

class Suivi_consommation(models.Model):
    mois = models.CharField(max_length=10,verbose_name="Mois")
    montantVoix = models.FloatField(verbose_name="Montant Voix")
    montantData = models.FloatField(verbose_name="Montant Data")
    forfait = models.ForeignKey(Forfait,on_delete=models.SET_NULL,null=True,verbose_name="Forfait")
    sim = models.ForeignKey(Sim,on_delete=models.SET_NULL,null=True,verbose_name="Numéro")

class Habilitation(models.Model):
    libellePage = models.CharField(max_length=60,verbose_name="Libelle Page")
    vRead = models.BooleanField(verbose_name="Affichage")
    vWrite = models.BooleanField(verbose_name="Création")
    vUpdate = models.BooleanField(verbose_name="Modification")
    vDelete = models.BooleanField(verbose_name="Suppression")
    profile = models.ForeignKey(Profil,on_delete=models.SET_NULL,null=True,verbose_name="Profil")

