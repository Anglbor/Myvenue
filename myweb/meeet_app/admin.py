from django.contrib import admin
from .models import Venue
from .models import MyUsers
from .models import Meet


# admin.site.register(Venue)
admin.site.register(MyUsers)
# admin.site.register(Meet)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone',)
    ordering = ('name',)
    search_fields = ('name', 'address')

@admin.register(Meet)
class MeetAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'meet_date', 'description', 'manager')
    list_display = ('name', 'venue', 'meet_date',)
    list_filter = ('venue', 'meet_date')
    ordering = ('meet_date',)
    search_fields = ('meet_date', 'venue')