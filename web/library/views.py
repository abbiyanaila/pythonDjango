from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

class AdminAccessView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class StaffAccessView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


