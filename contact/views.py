from django.shortcuts import render
from .forms import ContactForm


def contact(request):

    enviado = False

    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            # Los datos pasaron las validaciones
            enviado = True

            # Limpiar el formulario
            contact_form = ContactForm()

    else:
        contact_form = ContactForm()

    return render(request, "contact/contact.html", {
        "form": contact_form,
        "enviado": enviado
    })
