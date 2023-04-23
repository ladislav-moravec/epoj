from django.shortcuts import render, HttpResponse

from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "index.html",
                  dict(nazev_klienta="Petr Nový", typ_pojisteni="Povinné ručení", pojistovna="Generali Česká pojišťovna"))


