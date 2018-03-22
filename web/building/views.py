# redirect apa ya
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from building.models import Building
from building.forms import BuildingForm

# Create your views here.
# ini adalah class yang akan di eksekusi pada url, pemanggilannya harus sesuai dengan nama class

class BuildingList(View):
    def get(self, request):
        templateName = 'building/list.html' #pemanggilan ke list.html
        data = {
            'buildings': Building.objects.all(),
        }
        return render(request, templateName, data)

class BuildingAdd(View):
    def get(self, request):
        templateName = 'building/add.html' #pemanggilan ke add.html
        form = BuildingForm(request.POST or None)

        data = {
            'form' : form,
        }
        return render(request, templateName, data)

class BuildingSave(View):
    def post(self, request):
        templateName = 'building/add.html' #pemanggilan ke building add.html
        form = BuildingForm(request.POST or None)
        if form.is_valid(): #ngecek apakah data sudah terisi semua atau belum makanya dibilang is valid
            b = Building()
            b.nama = form.cleaned_data['nama']
            b.luas = form.cleaned_data['luas']
            b.fasilitas = form.cleaned_data['fasilitas']
            b.save()
        else:
            data = {
                'form': form,
            }
            return render(request, templateName, data)
            
        return redirect('building:list')


class BuildingEdit(View):
    def get(self, request, pk):
        templateName = 'building/edit.html' #pemanggilan ke building edit.html
        b = Building.objects.get(pk=pk)
        building_init ={
            'nama': b.nama,
            'luas': b.luas,
            'fasilitas': b.fasilitas
        }
        form = BuildingForm(request.POST or None, initial=building_init)
        data = {
            'form' : form,
            'id': pk,
        }
        return render(request, templateName, data)


class BuildingUpdate(View):
    def post(self, request, pk):
        templateName = 'building/edit.html' #pemanggilan ke building edit.html
        form = BuildingForm(request.POST or None)
        if form.is_valid(): #ngecek apakah data sudah terisi semua atau belum makanya dibilang is valid
            b = Building.objects.get(pk=pk)
            b.nama = form.cleaned_data['nama']
            b.luas = form.cleaned_data['luas']
            b.fasilitas = form.cleaned_data['fasilitas']
            b.save(force_update=True)
        else:
            data = {
                'form': form,
                'id': pk,
            }
            return render(request, templateName, data)
            
        return redirect('building:list')

class BuildingDelete(View): 
    def get(self, request, pk):
        b = Building.objects.get(pk=pk)
        b.delete()
        return redirect('building:list')
