from unittest.mock import patch

from django.test import TestCase, Client

from djangotesting.api.models import Person
from djangotesting.api.serializers import PersonSerializer


class PersonViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        Person.objects.create(first_name="John", last_name="Smith", job_title="developer")
        Person.objects.create(first_name="Jane", last_name="Smith")
        Person.objects.create(first_name="Rowan", last_name="Atkinson")

    def test_get_all_people_should_return_all_people(self):
        response = self.client.get("/people/")
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)

        self.assertEqual(response.data, serializer.data)

    def test_get_individual_person_should_return_single_person(self):
        special_person = Person.objects.create(first_name="Penn", last_name="Teller", job_title="magician")
        response = self.client.get(f"/people/{special_person.id}/")
        serializer = PersonSerializer(special_person, many=False)

        self.assertEqual(response.data, serializer.data)

    @patch('djangotesting.api.models.Person.get_greeting')
    def test_get_person_greeting_should_call_person_greeting(self, get_greeting):
        special_person = Person.objects.create(first_name="Penn", last_name="Teller", job_title="magician")
        get_greeting.return_value = f"Hello!"

        response = self.client.get(f"/people/{special_person.id}/greet/")

        self.assertEqual(response.data, "Hello!")
        self.assertEqual(response.status_code, 200)

    def test_get_non_existent_person_greeting_should_return_not_found(self):
        response = self.client.get(f"/people/99999/greet/")

        self.assertEqual(response.status_code, 404)
