from rest_framework.views import APIView, Request, Response
from .base_views import ListBaseView, CreateBaseView


class GenericBaseView(APIView):
    view_queryset = None
    view_serializer = None


class ListGenericView(ListBaseView, GenericBaseView):
    def get(self, request: Request) -> Response:
        return super().list(request)


class CreateGenericView(CreateBaseView, GenericBaseView):
    def post(self, request: Request) -> Response:
        return super().create(request)