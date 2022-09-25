from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class TestAPIView(APIView):
    """Test API's"""

    serializer_class = serializers.TestSerializer

    def post(self, req):
        """Hello message with name"""

        serializer = self.serializer_class(data=req.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"

            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, req, format=None):
        an_api_view = [
            "POST",
            "GET",
            "PUT",
            "PATCH",
            "DELETE",
            "Request",
            1,
            None,
            {"source": "DICT"},
        ]
        return Response(
            {"code": 200, "status": True, "message": "OK", "data": an_api_view},
            status=status.HTTP_200_OK,
        )

    def put(self, req, pk=None):
        return Response({"method": "PUT"})

    def patch(self, req, pk=None):
        return Response({"method": "PATCH"})

    def delete(self, req, pk=None):
        return Response({"method": "DELETE"})


class TestAPIViewset(ViewSet):
    serializer_class = serializers.TestSerializer

    def create(self, req, format=None):
        serializer = self.serializer_class(data=req.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"

            return Response({"message": message}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, req, format=None):
        an_api_view_set = [
            "create() => POST",
            "list() => GET All Objects",
            "retrieve() => GET Single Object",
            "update() => PUT",
            "partial_update() => PATCH",
            "destroy() => DELETE",
            1,
            None,
            {"source": "DICT"},
        ]
        return Response(
            {"code": 200, "status": True, "message": "OK", "data": an_api_view_set},
            status=status.HTTP_200_OK,
        )

    def retrieve(self, req, pk=None):
        return Response({"method": "GET"})

    def update(self, req, pk=None):
        return Response({"method": "PUT"})

    def partial_update(self, req, pk=None):
        return Response({"method": "PATCH"})

    def destroy(self, req, pk=None):
        return Response({"method": "DELETE"})
