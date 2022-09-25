from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("view-set-2", views.TestAPIViewset, basename="view-set-2")

urlpatterns = [
    # WAY 1.1 - API using APIView - POST | GET | PUT | PATCH | DELETE
    path("api-view/", views.TestAPIView.as_view(), name="api-view"),
    # WAY 2.1 - API using Viewset - create() | list() | retrieve() | update() | partial_update() | destroy()
    path(
        "view-set-1/",
        views.TestAPIViewset.as_view(
            {
                "post": "create",
                "get": "list",
                # "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="api-view-set",
    ),
    # WAY 2.2 - API using Viewset - create() | list() | retrieve() | update() | partial_update() | destroy()
    path("", include(router.urls)),
]

"""
=> http://127.0.0.1:8000/api/profiles/api-view/
=> http://127.0.0.1:8000/api/profiles/view-set-1/
=> http://127.0.0.1:8000/api/profiles/view-set-2/

"""
