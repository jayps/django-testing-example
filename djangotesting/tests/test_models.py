from django.test import TestCase

from djangotesting.api.models import Person


class PersonTest(TestCase):
    def test_get_greeting_when_called_should_return_greeting(self):
        person = Person.objects.create(first_name="John", last_name="Smith")
        greeting = person.get_greeting()

        self.assertEqual(greeting, "Hello, John Smith.")