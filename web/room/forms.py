from django.forms import ModelForm
from room.models import Room

# mengambil fields dari model yang akan di eksekusi di forms
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['nama', 'kapasitas', 'luas','building']

        