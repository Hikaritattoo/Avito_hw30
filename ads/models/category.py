from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, null=True, validators=[MinLengthValidator(5), MaxLengthValidator(10)])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
