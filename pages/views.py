from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.


def accueil(request):

    contexte = {
        "nom_projet": "BiblioLearn",

        "modules": [
            "Catalogue",
            "Comptes et rôles",
            "Emprunts",
            "Mini-cours"
        ],

        "nb_ressources": 15
    }

    return render(request, "pages/accueil.html", contexte)


def a_propos(request):

    equipe = [
        {
            "nom": "Membre 1",
            "role": "Développeur Backend"
        },
        {
            "nom": "Membre 2",
            "role": "Développeur Frontend"
        },
        {
            "nom": "Membre 3",
            "role": "Chef de projet"
        }
    ]

    contexte = {
        "version": "1.0",
        "date_tp": "Novembre 2026",
        "equipe": equipe
    }

    return render(request, "pages/a_propos.html", contexte)



def contact(request):

    message_confirmation = None

    if request.method == "POST":

        formulaire = ContactForm(request.POST)

        if formulaire.is_valid():

            nom = formulaire.cleaned_data["nom"]

            message_confirmation = (
                f"Merci {nom}, votre message a bien été reçu"
            )

            formulaire = ContactForm()

    else:
        formulaire = ContactForm()

    contexte = {
        "formulaire": formulaire,
        "message_confirmation": message_confirmation
    }

    return render(request, "pages/contact.html", contexte)
