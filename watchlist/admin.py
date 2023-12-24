from django.contrib import admin

# Register your models here.
from watchlist.models import Watchlist,StreamPlatform

admin.site.register(Watchlist)
admin.site.register(StreamPlatform)