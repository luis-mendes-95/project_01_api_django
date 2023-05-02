from rest_framework import permissions
from rest_framework.views import Request, View
from cpf_cnpj.models import CpfCnpj


class IsAdminOrCpfCnpjOwner(permissions.BasePermission):
    # def has_permission(self, request: Request, view: View):
    #     return request.user and request.user.is_authenticated

    def has_object_permission(
        self, request: Request, view: View, obj: CpfCnpj
    ):
        return request.user.is_superuser or request.user == obj.account
