from django import forms


class ContactForm(forms.Form):

    name = forms.CharField(
        label="Nombre",
        required=True,
        min_length=3,
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Ingresa tu nombre",
            "class": "form-control"
        }),
        error_messages={
            "required": "Debes ingresar tu nombre.",
            "min_length": "El nombre debe tener al menos 3 caracteres."
        }
    )

    email = forms.EmailField(
        label="Correo electrónico",
        required=True,
        widget=forms.EmailInput(attrs={
            "placeholder": "Ingresa tu correo electrónico",
            "class": "form-control"
        }),
        error_messages={
            "required": "Debes ingresar tu correo electrónico.",
            "invalid": "Ingresa un correo electrónico válido."
        }
    )

    content = forms.CharField(
        label="Mensaje",
        required=True,
        min_length=10,
        max_length=1000,
        widget=forms.Textarea(attrs={
            "placeholder": "Escribe tu mensaje",
            "rows": 4,
            "class": "form-control"
        }),
        error_messages={
            "required": "Debes escribir un mensaje.",
            "min_length": "El mensaje debe tener al menos 10 caracteres.",
            "max_length": "El mensaje no puede superar los 1000 caracteres."
        }
    )

    def clean_name(self):
        name = self.cleaned_data["name"].strip()

        if not any(letra.isalpha() for letra in name):
            raise forms.ValidationError(
                "El nombre debe contener letras."
            )

        return name
