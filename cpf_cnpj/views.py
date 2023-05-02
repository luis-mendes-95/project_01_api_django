from rest_framework import generics
from cpf_cnpj.permissions import IsAdminOrCpfCnpjOwner
from .serializers import CpfCnpjSerializer
from .models import CpfCnpj
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class CpfCnpjView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    # queryset = CpfCnpj.objects.all()
    serializer_class = CpfCnpjSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return CpfCnpj.objects.all()

        return CpfCnpj.objects.filter(account=self.request.user)

    def perform_create(self, serializer) -> None:
        # from ipdb import set_trace
        # set_trace()

        if self.request.user.is_staff == True or self.request.user.is_superuser == True:
            serializer.save(account=self.request.user)
        else:
            raise PermissionError("Usuário sem permissão para criar CPF/CNPJ")

        # serializer.save(account=self.request.user)


class CpfCnpjDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrCpfCnpjOwner]

    queryset = CpfCnpj.objects.all()
    serializer_class = CpfCnpjSerializer
