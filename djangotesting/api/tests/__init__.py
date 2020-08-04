from django.test import TestCase

from djangotesting.api.models import Person


class PersonTest(TestCase):
    def setUp(self) -> None:
        # Do some setup stuff here
        pass

    def test_should_return_greeting(self):
        person = Person.objects.create(first_name="John", last_name="Smith")
        greeting = person.get_greeting()

        self.assertEqual(greeting, "Hello, John Smith.")