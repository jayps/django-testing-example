from django.db import models


class Person(models.Model):
    JOB_TITLE_CHOICES = [
        ('developer', 'Developer'),
        ('business_analyst', 'BA'),
        ('tester', 'Tester'),
        ('magician', 'Magic person'),
    ]

    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    job_title = models.CharField(max_length=30, null=True, blank=True, choices=JOB_TITLE_CHOICES)

    def get_greeting(self):
        return f'Hello, {self.first_name} {self.last_name}.'
