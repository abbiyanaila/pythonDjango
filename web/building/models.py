from django.db import models

# Create your models here.
# membuat class dengan nama Building beserta fields dan karakteristiknya
class Building(models.Model):
    nama = models.CharField(max_length=255)
    luas = models.CharField(max_length=255)
    fasilitas = models.CharField(max_length=255)
    # test = models.ForeignKey(Building), anggap ini room

    # pemanggilan pada terminal
    def __str__(self):
        return self.nama
        
