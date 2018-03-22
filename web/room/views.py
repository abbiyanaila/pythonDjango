# redirect apa ya
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import View
from room.models import Room
from room.forms import RoomForm
from library.views import AdminAccessView
# Create your views here.
# ini adalah class yang akan di eksekusi pada url, pemanggilannya harus sesuai dengan nama class


class RoomList(AdminAccessView):
    def get(self, request):
        templateName = 'room/list.html' #pemanggilan ke list.html
        data = {
            'rooms': Room.objects.all(),
        }
        return render(request, templateName, data)

class RoomAdd(AdminAccessView):
    def get(self, request):
        templateName = 'room/add.html' #pemanggilan ke add.html
        form = RoomForm(request.POST or None)

        data = {
            'form' : form,
            'mode': 'add',
        }
        return render(request, templateName, data)

class RoomSave(AdminAccessView):
    def post(self, request):
        templateName = 'room/add.html' #pemanggilan ke building add.html
        form = RoomForm(request.POST or None)
        if form.is_valid(): #ngecek apakah data sudah terisi semua atau belum makanya dibilang is valid
            b = Room()
            b.nama = form.cleaned_data['nama']
            b.luas = form.cleaned_data['luas']
            b.kapasitas = form.cleaned_data['kapasitas']
            b.building = form.cleaned_data['building']
            b.save()
        else:
            data = {
                'form': form,
            }
            return render(request, templateName, data)
            
        return redirect('room:list')


class RoomEdit(AdminAccessView):
    def get(self, request, pk):
        templateName = 'room/edit.html' #pemanggilan ke building edit.html
        b = Room.objects.get(pk=pk)
        room_init ={
            'nama': b.nama,
            'luas': b.luas,
            'kapasitas': b.kapasitas,
            'building': b.building,
        }
        form = RoomForm(request.POST or None, initial=room_init)
        data = {
            'form' : form,
            'id': pk,
        }
        return render(request, templateName, data)


class RoomUpdate(AdminAccessView):
    def post(self, request, pk):
        templateName = 'room/edit.html' #pemanggilan ke building edit.html
        form = RoomForm(request.POST or None)
        if form.is_valid(): #ngecek apakah data sudah terisi semua atau belum makanya dibilang is valid
            b = Room.objects.get(pk=pk)
            b.nama = form.cleaned_data['nama']
            b.luas = form.cleaned_data['luas']
            b.kapasitas = form.cleaned_data['kapasitas']
            b.building = form.cleaned_data['building']
            b.save(force_update=True)
        else:
            data = {
                'form': form,
                'id': pk,
            }
            return render(request, templateName, data)
            
        return redirect('room:list')

class RoomDelete(AdminAccessView): 
    def get(self, request, pk):
        b = Room.objects.get(pk=pk)
        b.delete()
        return redirect('room:list')
