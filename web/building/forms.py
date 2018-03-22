from django.forms import ModelForm
from building.models import Building

# mengambil fields dari model yang akan di eksekusi di forms
class BuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = ['nama', 'luas', 'fasilitas']

        