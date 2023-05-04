
from django.db import models


# Create your models here.
class Compte_facturation(models.Model):
    libelle = models.CharField(max_length=40,verbose_name="Compte de facturation",)

class Ticket(models.Model):
    numero = models.CharField(max_length=50,verbose_name="Numéro ticket",)
    dateDemande = models.DateField(verbose_name="Date de demande")
    dateApprobation = models.DateField(verbose_name="Date d'approbation")
    compte_facturation = models.ForeignKey(Compte_facturation,on_delete=models.SET_NULL, null=True)

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
    libelle = models.BooleanField(verbose_name="Actif",default=True) 
    
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
    libelle = models.CharField(max_length=40,verbose_name="Classe",)
    etat = models.ForeignKey(Etat,on_delete=models.SET_NULL,null=True)
        
    def __str__(self):
        return self.libelle


class Collaborateur(models.Model):
    matricule = models.CharField(max_length=7,unique=True)
    nom = models.CharField(max_length=150,verbose_name="Nom")
    prenom = models.CharField(max_length=150,verbose_name="Prénoms")
    fonction = models.CharField(max_length=150,verbose_name="Fonction")
    division = models.ForeignKey(Division,on_delete=models.SET_NULL, null=True)
    departement = models.ForeignKey(Departement,on_delete=models.SET_NULL, null=True)
    site = models.ForeignKey(Site,on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Service,on_delete=models.SET_NULL, null=True)
    classe = models.ForeignKey(Classe,on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.matricule
    
class Operateur(models.Model):
    identifiant = models.IntegerField()
    libelle = models.CharField(max_length=20,verbose_name="Opérateur")
    
    def __str__(self):
        return self.libelle

class Acces_sim(models.Model):
    libelle = models.CharField(max_length=20,verbose_name="Acces")
    
    def __str__(self):
        return self.libelle

class Type_sim(models.Model):
    libelle = models.CharField(max_length=20,verbose_name="type SIM")
    
    def __str__(self):
        return self.libelle

class Forfait(models.Model):
    libelle = models.CharField(max_length=20,verbose_name="Forfait")
    montant = models.IntegerField()
    montantPlafondVoix = models.IntegerField()
    montantPlafondData = models.IntegerField()
    plafondInterne = models.IntegerField()
    typeSim = models.ForeignKey(Type_sim,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.libelle
    
class Sim(models.Model):
    numero = models.IntegerField(verbose_name="Numéro")
    adresseIP = models.IntegerField(verbose_name="Adresse IP")
    operateur = models.ForeignKey(Operateur,on_delete=models.SET_NULL,null=True)
    forfait = models.ForeignKey(Forfait,on_delete=models.SET_NULL,null=True)
    acces = models.ForeignKey(Acces_sim,on_delete=models.SET_NULL,null=True)
    etat = models.ForeignKey(Etat,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.numero

class Affectation_sim(models.Model):
    dateAffectation = models.DateField(verbose_name="Date d'affectaion",auto_now=True)
    dateActivation = models.DateField(verbose_name="Date d'activation",auto_now=True)
    dateDesactivation = models.DateField(verbose_name="Date désactivation",auto_now=True)
    dateModification = models.DateField(verbose_name="Date de Modification",auto_now=True)
    collaborateur = models.ForeignKey(Collaborateur,on_delete=models.SET_NULL,null=True) 
    ticket = models.ForeignKey(Ticket,on_delete=models.SET_NULL,null=True)
    sim = models.ForeignKey(Sim,on_delete=models.SET_NULL,null=True)

class Suivi_consommation(models.Model):
    mois = models.CharField(max_length=10,verbose_name="Mois")
    montantVoix = models.FloatField(verbose_name="Montant Voix")
    montantData = models.FloatField(verbose_name="Montant Data")
    forfait = models.ForeignKey(Forfait,on_delete=models.SET_NULL,null=True)
    sim = models.ForeignKey(Sim,on_delete=models.SET_NULL,null=True)

class Habilitation(models.Model):
    libellePage = models.CharField(max_length=60,verbose_name="Libelle Page")
    vRead = models.BooleanField(verbose_name="Affichage")
    vWrite = models.BooleanField(verbose_name="Création")
    vUpdate = models.BooleanField(verbose_name="Modification")
    vDelete = models.BooleanField(verbose_name="Suppression")
    profile = models.ForeignKey(Profil,on_delete=models.SET_NULL,null=True)
    