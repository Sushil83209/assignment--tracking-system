from django.urls import path
from .views import AssignmentViewSet

urlpatterns = [
    # GET /api/assignment/
    # POST /api/assignment/
    path(
        "",
        AssignmentViewSet.as_view({
            "get": "list",
            "post": "create",
        })
    ),

    # PUT/PATCH /api/assignment/{id}/ -> update one
    # DELETE /api/assignment/{id}/ -> delete one
    path(
        "<int:pk>/",
        AssignmentViewSet.as_view({
            "put": "update",
            "patch": "update",
            "delete": "destroy",
        })
    ),
]