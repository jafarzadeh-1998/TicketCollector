from django.contrib import admin
from . import models

@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('context' ,'rate' ,'pub_date')
    fieldsets = (
        ('Ticket', {
            'fields': ('context',)
        }),
    )