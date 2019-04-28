from django.shortcuts import render ,HttpResponse ,get_object_or_404
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect

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

def VotePage(request ,pk):
    ticket = get_object_or_404(models.Ticket, pk = pk)
    
    if request.method == 'POST':
        ticket.rate = ticket.rate+1
        ticket.save()
        return HttpResponseRedirect(reverse('ticket:ticket-detail' ,args=[str(pk)]) )
    
    else:
        context = {
            'context' : ticket.context,
            'rate'    : ticket.rate, 
        }
    
    return render(request ,'ticket/vote_page.html' ,context)
