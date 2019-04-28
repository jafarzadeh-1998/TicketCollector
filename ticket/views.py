from django.shortcuts import render ,HttpResponse
from django.views import generic

from . import models


class Index(generic.TemplateView):
    template_name='./ticket/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticketCount'] = models.Ticket.objects.all().count()
        return context
    

class TicketDetail(generic.DetailView):
    template_name = './ticket/ticket_detail.html'
    model = models.Ticket

class TicketList(generic.ListView):
    model = models.Ticket
    template_name = "./ticket/ticket_list.html"