from django.db import models
from building.models import Building

# Create your models here.
# membuat class dengan nama Building beserta fields dan karakteristiknya
class Room(models.Model):
    nama = models.CharField(max_length=255)
    kapasitas = models.CharField(max_length=255)
    luas = models.CharField(max_length=255)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama