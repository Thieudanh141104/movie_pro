from django.contrib import admin
from django.contrib.auth.models import Group
from app.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Room)
admin.site.register(Screening)
admin.site.register(Seat)
admin.site.register(Booking)
admin.site.unregister(Group)
