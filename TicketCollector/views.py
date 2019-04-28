from django.shortcuts import render ,HttpResponse
from django.views import generic
from django.contrib.auth.models import User


class profile(generic.TemplateView):

    template_name='profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = User.first_name
        return context