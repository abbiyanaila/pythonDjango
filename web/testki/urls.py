from django.conf.urls import url
from testki.views import *

# memanggil url yang akan di gunakan di browser, yang di ambil pada class dalam view.py
urlpatterns = [
    # url(r'list$', TestXiList.as_view(), name='list'),
    url(r'add$', TestKiAdd.as_view(), name='add'),
    url(r'save$', TestKiSave.as_view(), name='save'),
]