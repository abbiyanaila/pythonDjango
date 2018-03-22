from django import forms

class TestKiForm(forms.Form):
    alas = forms.CharField(label='Alas Segitiga', max_length=25)
    tinggi = forms.CharField(label='Tinggi Segitiga', max_length=15)
    