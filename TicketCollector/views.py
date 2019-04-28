from django.shortcuts import render ,HttpResponse
from django.views import generic


class Index(generic.TemplateView):

    template_name='base_generic.html'
    # return HttpResponse
    # render(request ,'index.html' ,{})