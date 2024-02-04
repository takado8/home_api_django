from django.db import models


class TestItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f'TestItem(name={self.name}, description={self.description})'
