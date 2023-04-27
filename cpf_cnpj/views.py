from rest_framework.views import APIView, Request, Response, status
from .serializers import CpfCnpjSerializer
from .models import CpfCnpj
from django.shortcuts import get_object_or_404


class CpfCnpjView(APIView):
    def get(self, request: Request) -> Response:
        all_cpf_cnpj = CpfCnpj.objects.all()
        serializer = CpfCnpjSerializer(all_cpf_cnpj, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = CpfCnpjSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class CpfCnpjDetailView(APIView):
    def get(self, request: Request, pk: int) -> Response:
        cpf_cnpj = get_object_or_404(CpfCnpj, pk=pk)
        serializer = CpfCnpjSerializer(cpf_cnpj)

        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, pk: int) -> Response:
        cpf_cnpj = get_object_or_404(CpfCnpj, pk=pk)
        serializer = CpfCnpjSerializer(cpf_cnpj, request.data, partial=True)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, pk: int) -> Response:
        cpf_cnpj = get_object_or_404(CpfCnpj, pk=pk)
        cpf_cnpj.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)