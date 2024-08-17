from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(max_length=30, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.title
