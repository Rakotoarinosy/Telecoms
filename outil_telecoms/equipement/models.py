from logging import PlaceHolder
from django.db import models

from sim.models import Collaborateur, Etat, Sim, Ticket

# Create your models here.
class Bc(models.Model):
    reference_bc = models.CharField(verbose_name="Bon de commande",max_length=50)
    date_bc = models.DateField(verbose_name="Date Bon de commande")
    def __str__(self):
        return self.reference_bc

class Categorie(models.Model):
    libelle = models.CharField(max_length=30, verbose_name="Catégorie",default="TELECOM")
    def __str__(self):
        return self.libelle

class Facture(models.Model):
    num_facture = models.CharField(max_length=60,verbose_name="Numéro facture")
    dateFacture = models.DateField(verbose_name="Date facture")
    def __str__(self):
        return self.num_facture

class Emplacement(models.Model):
    libelle = models.CharField(verbose_name="Emplacement",max_length=50)
    def __str__(self):
        return self.libelle
    
class Emplacement_article (models.Model):
    emplacement = models.ForeignKey(Emplacement,on_delete=models.SET_NULL,null=True )
    def __str__(self):
        return self.emplacement
       
class Code_analytique(models.Model):
    libelle = models.CharField(verbose_name="Code Analytique",max_length=50)
    categorie = models.ForeignKey(Categorie,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.libelle

class Materiel(models.Model):
    libelle = models.CharField(verbose_name="Type d'équipement",max_length=50)
    code_analytique = models.ForeignKey(Code_analytique,on_delete=models.SET_NULL,null=True)
    def __str__ (self):
        return self.libelle

class Article_modele(models.Model):
    reference_modele = models.CharField(max_length=60, verbose_name="Modèle équipement")
    materiel = models.ForeignKey(Materiel,on_delete=models.SET_NULL,null=True)     
    def __str__ (self):
        return self.reference_modele

class Article(models.Model):
    imei1 = models.IntegerField(verbose_name="IMEI 1")
    imei2 = models.IntegerField(verbose_name="IMEI 2",blank=False,null=True)
    imei3 = models.IntegerField(verbose_name="IMEI 3",blank=False,null=True)
    imei4 = models.IntegerField(verbose_name="IMEI 4",blank=False,null=True)
    etat = models.ForeignKey(Etat,on_delete=models.SET_NULL,null=True)
    article_modele = models.ForeignKey(Article_modele,on_delete=models.SET_NULL,null=True)

class Reception_article(models.Model):
    article_modele = models.ForeignKey(Article_modele,on_delete=models.SET_NULL,null=True)
    quantite = models.IntegerField(verbose_name="Quantité")
    pu_ht = models.IntegerField(verbose_name="Prix Hors Taxe")
    prix_global = models.IntegerField(verbose_name="Prix global")
    facture = models.ForeignKey(Facture,on_delete=models.SET_NULL,null=True)
    bc = models.ForeignKey(Bc,on_delete=models.SET_NULL,null=True)

class Sortie(models.Model):
    quantiteSortie = models.IntegerField(verbose_name="Quantité Sortie")
    numBonSortie = models.IntegerField(verbose_name="Numéro Bon de sortie")
    numSortie = models.IntegerField(verbose_name="Numéro de sortie")
    reception_article = models.ForeignKey(Reception_article,on_delete=models.SET_NULL,null=True)

class Affectation_article(models.Model):
    dateAffectation = models.DateField(verbose_name="Dade d'affectaion",auto_now=True)
    dateDesactivation = models.DateField(verbose_name="Dade d'affectaion",blank=True,null=True)
    collaborateur = models.ForeignKey(Collaborateur,on_delete=models.SET_NULL,null=True)
    ticket = models.ForeignKey(Ticket,on_delete=models.SET_NULL,null=True)
    article = models.ForeignKey(Article,on_delete=models.SET_NULL,null=True)
    sortie = models.ForeignKey(Sortie,on_delete=models.SET_NULL,null=True)
    
class Article_sim(models.Model):
    affectation_article = models.ForeignKey(Affectation_article,on_delete=models.SET_NULL,null=True)
    sim = models.ForeignKey(Sim,on_delete=models.SET_NULL,null=True)    
