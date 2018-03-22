# redirect apa ya
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from testki.forms import TestKiForm


# Create your views here.
# ini adalah class yang akan di eksekusi pada url, pemanggilannya harus sesuai dengan nama class

# class TestXiList(View):
#     def get(self, request):
#         templateName = 'room/list.html' #pemanggilan ke list.html
#         data = {
#             'rooms': Room.objects.all(),
#         }
#         return render(request, templateName, data)

class TestKiAdd(View):
    def get(self, request):
        templateName = 'testki/add.html' #pemanggilan ke add.html
        form = TestKiForm(request.POST or None)

        data = {
            'form' : form,
            'mode': 'add',
            'luas': 0,
        }
        return render(request, templateName, data)

class TestKiSave(View):
    def post(self, request):
        templateName = 'testki/add.html' #pemanggilan ke building add.html
        alas, tinggi, luas = 0.0, 0.0, 0.0
        form = TestKiForm(request.POST or None)
        if form.is_valid(): #ngecek apakah data sudah terisi semua atau belum makanya dibilang is valid
           alas = form.cleaned_data['alas']
           tinggi = form.cleaned_data['tinggi']
           luas = 0.5 * float(alas) * float(tinggi)
        data = {
            'form': form,
            'luas': luas,
            'mode': 'save',
        }
        return render(request, templateName, data)
            
        return redirect('room:list')