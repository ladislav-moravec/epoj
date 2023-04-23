from django import forms
from .models import Client, Tag, Uzivatel


class ClientForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)

    class Meta:
        model = Client
        fields = ["client", "insurance", "insurance_type", "tags"]


class UzivatelForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = Uzivatel
        fields = ["email", "password"]


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ["email", "password"]
