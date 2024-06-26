from django import forms
from coffee.models import ContactModel


class ContactModelForm(forms.ModelForm):

    class Meta:
        model = ContactModel
        fields = ["name", "email", "phone", "message"]