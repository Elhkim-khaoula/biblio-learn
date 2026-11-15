
from django import forms


class ContactForm(forms.Form):

    nom = forms.CharField(
        label="Votre nom",
        max_length=100
    )

    email = forms.EmailField(
        label="Votre adresse email"
    )

    message = forms.CharField(
        label="Votre message",
        widget=forms.Textarea
    )
