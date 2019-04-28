from django.contrib import admin
from django.urls import path ,include 
from django.conf.urls import url
from . import views

app_name = 'ticket'
urlpatterns = [
    path('', views.Index.as_view() ,name= 'index'),
    path('list', views.TicketList.as_view() ,name='list'),
    url(r'^detail/(?P<pk>\d+)$', views.TicketDetail.as_view() ,name= 'ticket-detail'),
    url(r'^vote/(?P<pk>\d+)$', views.VotePage ,name= 'vote-ticket'),
]