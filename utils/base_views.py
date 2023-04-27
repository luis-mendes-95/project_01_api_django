from rest_framework.views import APIView, Request, Response, status


class ListBaseView(APIView):
    def list(self, request: Request) -> Response:
        queryset = self.view_queryset.all()
        serializer = self.view_serializer(queryset, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class CreateBaseView(APIView):
    def create(self, request: Request) -> Response:
        serializer = self.view_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)