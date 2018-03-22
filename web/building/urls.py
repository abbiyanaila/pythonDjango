from django.conf.urls import url
from building.views import *

# memanggil url yang akan di gunakan di browser, yang di ambil pada class dalam view.py
urlpatterns = [
    url(r'list$', BuildingList.as_view(), name='list'),
    url(r'add$', BuildingAdd.as_view(), name='add'),
    url(r'save$', BuildingSave.as_view(), name='save'),
    url(r'delete/(?P<pk>\d+)$', BuildingDelete.as_view(), name='delete'),
    url(r'edit/(?P<pk>\d+)$', BuildingEdit.as_view(), name='edit'),
    url(r'update/(?P<pk>\d+)$', BuildingUpdate.as_view(), name='update'),
]