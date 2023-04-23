from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class InsuranceType(models.Model):
    insurance_type = models.CharField(max_length=80)

    def __str__(self):
        return "Typ pojištění: {0}".format(self.insurance_type)


class Tag(models.Model):
    tag_title = models.CharField(max_length = 30, verbose_name="Tagy")

    def __str__(self):
        return self.tag_title

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tagy"


class Client(models.Model):
    client = models.CharField(max_length=200, verbose_name="Jméno a příjmení klienta")
    insurance = models.CharField(max_length=200, default='', verbose_name="Pojišťovna")
    insurance_type = models.ForeignKey(InsuranceType, on_delete=models.SET_NULL, null=True,
                                       verbose_name="Typ pojištění")
    tags = models.ManyToManyField(Tag)

    def __init__(self, *args, **kwargs):
        super(Client, self).__init__(*args, **kwargs)

    def __str__(self):
        tags = [i.tag_title for i in self.tags.all()]
        return "Jméno klienta: {0} | Pojišťovna: {1} | Typ pojištění: {2} | Tagy: {3}".format(self.client, self.insurance,
                                                                                    self.insurance_type, self.tags)


class UzivatelManager(BaseUserManager):
    # Vytvoří uživatele
    def create_user(self, email, password):
        print(self.model)
        if email and password:
            user = self.model(email=self.normalize_email(email))
            user.set_password(password)
            user.save()
        return user

    # Vytvoří admina
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save()
        return user


class Uzivatel(AbstractBaseUser):

    email = models.EmailField(max_length = 300, unique=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        verbose_name = "uživatel"
        verbose_name_plural = "uživatelé"

    objects = UzivatelManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return "email: {}".format(self.email)

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


