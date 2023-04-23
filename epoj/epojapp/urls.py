from django.urls import path
from . import views

urlpatterns = [
    path('client_index/', views.ClientIndex.as_view(), name='client_index'),
    path("<int:pk>/client_detail/", views.CurrentClientView.as_view(), name='client_detail'),
    path("create_client/", views.CreateClient.as_view(), name="new_client"),
    path("<int:pk>/edit/", views.EditClient.as_view(), name="edit_client"),
    path("register/", views.UzivatelViewRegister.as_view(), name = "registrace"),
    path("login/", views.UzivatelViewLogin.as_view(), name = "login"),
    path("logout/", views.logout_user, name = "logout"),
]
