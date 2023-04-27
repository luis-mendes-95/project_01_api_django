from rest_framework.views import APIView, Request, Response, status

from .serializers import AccountSerializer
from .models import Account

from django.shortcuts import get_object_or_404

from utils.base_views import ListBaseView, CreateBaseView


class AccountView(ListBaseView, CreateBaseView):
    view_queryset = Account.objects.all()
    view_serializer = AccountSerializer


class AccountDetailView(APIView):
    def get(self, request: Request, pk: int) -> Response:
        account = get_object_or_404(Account, pk=pk)
        serializer = AccountSerializer(account)

        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, pk: int) -> Response:
        account = get_object_or_404(Account, pk=pk)
        serializer = AccountSerializer(account, request.data, partial=True)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, pk: int) -> Response:
        account = get_object_or_404(Account, pk=pk)
        account.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)