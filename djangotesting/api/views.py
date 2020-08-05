from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from djangotesting.api.models import Person
from djangotesting.api.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    filterset_fields = ('job_title',)

    @action(methods=['GET'], detail=True)
    def greet(self, request, pk):
        try:
            person = Person.objects.get(pk=pk)
            return Response(data=person.get_greeting())
        except Person.DoesNotExist:
            return Response(data=None, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['PUT'], detail=True)
    def make_developer(self, request, pk):
        try:
            person = Person.objects.get(pk=pk)
            person.job_title = "developer"
            person.save()
            serializer = PersonSerializer(person, many=False)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Person.DoesNotExist:
            return Response(data=None, status=status.HTTP_404_NOT_FOUND)
