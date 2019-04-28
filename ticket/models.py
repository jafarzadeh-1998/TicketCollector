from django.db import models
from django.urls import reverse

class Ticket(models.Model):
    context  = models.CharField( max_length=300)
    pub_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    rate     = models.IntegerField(default=0)

    def __str__ (self):
        return self.context

    def get_absolute_url(self):
        return reverse('ticket:ticket-detail', args=[str(self.id)])