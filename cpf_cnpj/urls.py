from django.urls import path
from .views import CpfCnpjView, CpfCnpjDetailView

urlpatterns = [
    path("cpf-cnpj/", CpfCnpjView.as_view()),
    path("cpf-cnpj/<int:pk>", CpfCnpjDetailView.as_view()),
]