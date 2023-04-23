from django.db import models

class Client(models.Model):
    client = models.CharField(max_length=200)
    home_adress = models.CharField(max_length=180)

    def __str__(self):
        return "Jméno klienta: {0} | Domovská adresa: {1}".format(self.client, self.home_adress)



class HomeAdress(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    typ_pojisteni = models.CharField(max_length=80)

    def __str__(self):
        return "Jméno klienta: {0} | Typ pojištění: {1}".format(self.client, self.typ_pojisteni)


