# Seperation of concern
from django.urls import path
from .views import AssignmentViewSet

urlpatterns = [
    # GET  /api/assignments/  -> list all assignments
    # POST /api/assignments/  -> create an assignment
    path(
        "",
    AssignmentViewSet.as_view({ "get": "list", "post": "create", })),
]