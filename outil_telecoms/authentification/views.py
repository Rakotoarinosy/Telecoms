from unicodedata import name
from django.shortcuts import render

from django.shortcuts import render
from .authentification import Database

# Create your views here.

def login(request):
    return render(request,'login.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        login = Database()
        auth_result = login.authentification(username, password)
        if auth_result == True:
            # L'authentification a réussi
            # Faites ce que vous voulez ici, par exemple rediriger vers une page d'accueil
            print("mandeh")
            return render(request, "home.html")
        else:
            # L'authentification a échoué
            # Afficher un message d'erreur
            print("erreur")
            return render(request, "login.html", {"error": "Nom d'utilisateur ou mot de passe incorrect"})
    else:
        # Afficher le formulaire de connexion
        return render(request, "login.html")