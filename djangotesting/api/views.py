from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from djangotesting.api.models import Person
from djangotesting.api.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    @action(methods=['GET'], detail=True)
    def greet(self, request, pk):
        person = Person.objects.get(pk=pk)
        return Response(data=person.get_greeting())