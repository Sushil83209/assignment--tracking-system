"""
views.py — the "brain" of the assignments app.
"""

from django.shortcuts import redirect, render

from rest_framework import status, viewsets
from rest_framework.response import Response

from .forms import AssignmentForm
from .models import Assignment
from .serializers import AssignmentSerializer


def assignment_list(request):
    """
    Show the add assignment form and the list of assignments.
    """

    # POST request
    if request.method == "POST":

        # Put submitted data into the form
        form = AssignmentForm(request.POST)

        if form.is_valid():

            # Save assignment to database
            form.save()

            # Redirect after successful POST
            return redirect("assignments:assignment_list")

    # GET request
    else:
        form = AssignmentForm()

    # Get all assignments
    assignments = Assignment.objects.all()

    # Render HTML page
    return render(
        request,
        "assignments/assignment_list.html",
        {
            "form": form,
            "assignments": assignments,
        },
    )


# ---------------------------------------------------------------------
# REST API
# ---------------------------------------------------------------------

class AssignmentViewSet(viewsets.GenericViewSet):
    """
    CRUD API for assignments.

    GET     /api/assignments/          -> list all
    POST    /api/assignments/          -> create one
    PUT     /api/assignments/{id}/     -> update one
    PATCH   /api/assignments/{id}/     -> partially update one
    DELETE  /api/assignments/{id}/     -> delete one
    """

    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    # GET /api/assignments/
    def list(self, request):
        """Return every assignment."""

        assignments = Assignment.objects.all()

        serializer = AssignmentSerializer(
            assignments,
            many=True
        )

        return Response(serializer.data)

    # POST /api/assignments/
    def create(self, request):
        """Create a new assignment."""

        serializer = AssignmentSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # PUT / PATCH /api/assignments/{id}/
    def update(self, request, pk=None):
        """Update an existing assignment."""

        # Find the assignment
        assignment = self.get_object()

        # PATCH = partial update
        # PUT = full update
        partial = request.method == "PATCH"

        serializer = AssignmentSerializer(
            assignment,
            data=request.data,
            partial=partial
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # DELETE /api/assignments/{id}/
    def destroy(self, request, pk=None):
        """Delete an assignment."""

        assignment = self.get_object()

        assignment.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )