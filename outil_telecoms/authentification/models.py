# from __future__ import division
# from pickle import TRUE
# from django.db import models
# from django.contrib.auth.models import AbstractUser


# # Create your models here.
# class User(AbstractUser):
#     matricule = models.CharField(max_length=7,unique=True)
#     nom = models.CharField(max_length=150,verbose_name="Nom")
#     prenom = models.CharField(max_length=150,verbose_name="Prénoms")
#     fonction = models.CharField(max_length=150,verbose_name="Fonction")
#     # division = models.ForeignKey("Division",on_delete=models.SET_NULL,)
#     # departement = models.ForeignKey("Departement",on_delete=models.SET_NULL,)
#     # site = models.ForeignKey("Site",on_delete=models.SET_NULL,)
#     # service = models.ForeignKey("Service",on_delete=models.SET_NULL,)
#     # classe = models.ForeignKey("Classe",on_delete=models.SET_NULL,)
#     username = None
#     first_name = None
#     last_name = None
#     email = None
    
#     USERNAME_FIELD = "matricule"
        
#     def __str__(self):
#         return self.matricule
    
# class Division:
#     division = models.CharField(max_length=10,verbose_name="Division",)

# class Departement:
#     libelle = models.CharField(max_length=40,verbose_name="Département",)

# class Site:
#     libelle = models.CharField(max_length=40,verbose_name="Site",)

# class Service:
#     libelle = models.CharField(max_length=40,verbose_name="Service",)
    
# class Classe:
#     libelle = models.CharField(max_length=40,verbose_name="Classe",)

# class Collaborateur(User):
#     division = models.ForeignKey(Division,on_delete=models.SET_NULL,)
#     departement = models.ForeignKey(Departement,on_delete=models.SET_NULL,)
#     site = models.ForeignKey(Site,on_delete=models.SET_NULL,)
#     service = models.ForeignKey(Service,on_delete=models.SET_NULL,)
#     classe = models.ForeignKey(Classe,on_delete=models.SET_NULL,)