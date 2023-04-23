
from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Client, Uzivatel
from .forms import ClientForm, UzivatelForm, LoginForm


class ClientIndex(generic.ListView):

    template_name = "epoj/client_index.html" # cesta k templatu ze složky templates (je možné sdílet mezi aplikacemi)
    context_object_name = "client" # pod tímto jménem budeme volat list objektů v templatu

# tato funkce nám získává list clientů seřazených od největšího id (9,8,7...)
    def get_queryset(self):
        return Client.objects.all().order_by("-id")


class CurrentClientView(generic.DetailView):

    model = Client
    template_name = "epoj/client_detail.html"


class CreateClient(LoginRequiredMixin, generic.edit.CreateView):

    form_class = ClientForm
    template_name = "epoj/create_client.html"

# Metoda pro GET request, zobrazí pouze formulář
    def get(self, request):
        if not request.user.is_admin:
            messages.info(request, "Nemáš práva pro přidání klienta.")
            return redirect(reverse("client_index"))
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

# Metoda pro POST request, zkontroluje formulář, pokud je validní vytvoří nový klient, pokud ne zobrazí formulář s chybovou hláškou
    def post(self, request):
        if not request.user.is_admin:
            messages.info(request, "Nemáš práva pro přidání klienta.")
            return redirect(reverse("client_index"))
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("client_index")
        return render(request, self.template_name, {"form": form})


class UzivatelViewRegister(generic.edit.CreateView):
    form_class = UzivatelForm
    model = Uzivatel
    template_name = "epoj/user_form.html"

    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "Už jsi přihlášený, nemůžeš se registrovat.")
            return redirect(reverse("client_index"))
        else:
            form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        if request.user.is_authenticated:
            messages.info(request, "Už jsi přihlášený, nemůžeš se registrovat.")
            return redirect(reverse("client_index"))
        form = self.form_class(request.POST)
        if form.is_valid():
            uzivatel = form.save(commit = False)
            password = form.cleaned_data["password"]
            uzivatel.set_password(password)
            uzivatel.save()
            login(request, uzivatel)
            return redirect("client_index")

        return render(request, self.template_name, {"form":form})


class UzivatelViewLogin(generic.edit.CreateView):
    form_class = LoginForm
    template_name = "epoj/user_form.html"

    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "Už jsi přihlášený, nemůžeš se přihlásit znovu.")
            return redirect(reverse("client_index"))
        else:
            form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        if request.user.is_authenticated:
            messages.info(request, "Už jsi přihlášený, nemůžeš se přihlásit znovu.")
            return redirect(reverse("client_index"))
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email = email, password = password)
            if user:
                login(request, user)
                return redirect("client_index")
            else:
                messages.error(request, "Tento účet neexistuje.")
        return render(request, self.template_name, {"form": form})


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        messages.info(request, "Nemůžeš se odhlásit, pokud nejsi přihlášený.")
    return redirect(reverse("login"))


class CurrentClientView(generic.DetailView):

    model = Client
    template_name = "epoj/client_detail.html"

    def get(self, request, pk):
        try:
            client = self.get_object()
        except:
            return redirect("client_index")
        return render(request, self.template_name, {"client" : client})

    def post(self, request, pk):
        if request.user.is_authenticated:
            if "edit" in request.POST:
                return redirect("edit_client", pk=self.get_object().pk)
            else:
                if not request.user.is_admin:
                    messages.info(request, "Nemáš práva pro smazání klienta.")
                    return redirect(reverse("client_index"))
                else:
                    self.get_object().delete()
        return redirect(reverse("client_index"))


class EditClient(LoginRequiredMixin, generic.edit.CreateView):
    form_class = ClientForm
    template_name = "epoj/create_client.html"

    def get(self, request, pk):
        if not request.user.is_admin:
            messages.info(request, "Nemáš práva pro úpravu klienta.")
            return redirect(reverse("client_index"))
        try:
            client = Client.objects.get(pk = pk)
        except:
            messages.error(request, "Tento klient neexistuje!")
            return redirect("client_index")
        form = self.form_class(instance=client)
        return render(request, self.template_name, {"form": form})

    def post(self, request, pk):
        if not request.user.is_admin:
            messages.info(request, "Nemáš práva pro úpravu klienta.")
            return redirect(reverse("client_index"))
        form = self.form_class(request.POST)

        if form.is_valid():
            client_name = form.cleaned_data["Jméno a příjmení"]
            insurance = form.cleaned_data["Pojišťovna"]
            insurance_type = form.cleaned_data["Typ pojištění"]
            tagy = form.cleaned_data["tagy"]
            try:
                client = Client.objects.get(pk = pk)
            except:
                messages.error(request, "Tento klient neexistuje!")
                return redirect(reverse("client_index"))
            client.client_name = client_name
            client.insurance = insurance
            client.insurance_type = insurance_type
            client.tagy.set(tagy)
            client.save()
        # return render(request, self.template_name, {"form":form})
        return redirect("client_detail", pk = client.id)
