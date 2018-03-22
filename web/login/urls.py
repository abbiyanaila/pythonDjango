from django.conf.urls import url
from login.views import *

# memanggil url yang akan di gunakan di browser, yang di ambil pada class dalam view.py
urlpatterns = [
    url(r'view$', LoginView.as_view(), name='view'),
    url(r'doLogin$', DoLogin.as_view(), name='dologin'),
    url(r'doLogout$', DoLogout.as_view(), name='dologout'),
]