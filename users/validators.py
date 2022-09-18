from django.core.exceptions import ValidationError
from rest_framework import serializers


def check_age(date_of_birth, date):
    today = date.today()
    age = today.date - date_of_birth
    if age < 9:
        raise ValidationError(f'Age {age} is not available for registration')


class EmailDomainValidator:
    def __int__(self, domains):
        if not isinstance(domains, list):
            domains = [domains]

        self.domains = domains

    def __call__(self, email):
        domain = email.split('@')[1]
        if domain in self.domains:
            raise serializers.ValidationError(f'Domain could not be {domain}')



