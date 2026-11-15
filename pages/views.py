from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def accueil(request):
    contexte = {
        "nom_projet": "BiblioLearn",
        "modules": ["Catalogue", "Comptes et rôles", "Emprunts", "Mini-cours"],
    }
    return render(request, "pages/accueil.html", contexte)

def a_propos(request):
    contexte = {
        "version": "1.0",
        "date_tp": "Novembre 2026"
    }

    return render(request, "pages/a_propos.html", contexte)