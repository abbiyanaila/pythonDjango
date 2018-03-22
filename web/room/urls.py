efrom django.conf.urls import url
from room.views import *

# memanggil url yang akan di gunakan di browser, yang di ambil pada class dalam view.py
urlpatterns = [
    url(r'list$', RoomList.as_view(), name='list'),
    url(r'add$', RoomAdd.as_view(), name='add'),
    url(r'save$', RoomSave.as_view(), name='save'),
    url(r'delete/(?P<pk>\d+)$', RoomDelete.as_view(), name='delete'),
    url(r'edit/(?P<pk>\d+)$', RoomEdit.as_view(), name='edit'),
    url(r'update/(?P<pk>\d+)$', RoomUpdate.as_view(), name='update'),
]