from typing import Any
from django.db import models
from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .models import BaseUser, Profile
from django.views.generic import FormView, ListView, DetailView, UpdateView
from django.views import View
from django.contrib.auth import login 
from .forms import RegistrationForm

class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = RegistrationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        print(form)
        user = form.save()
        if user:
            login(self.request, user)
            query = Profile.objects.create(user = self.request.user, bio="Hello World")

        return super(RegisterView, self).form_valid(form)
    
    
class ProfileView(DetailView):
    model = Profile
    template_name = 'users/profile.html'
    context_object_name = 'object' 

    def get_object(self, queryset=None):
        return BaseUser.objects.get(email=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    


# i think this section need payment to change status
class UpdatePermissions(View):
    def post(self,request):
        special_month = request.POST.get("special_month")
        query = BaseUser.objects.filter(email=self.request.user).update(is_sepecial_month=special_month)
        return HttpResponseRedirect(reverse("users:profile")) 
