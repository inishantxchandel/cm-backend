from django.contrib import admin
from .models import Campaign,Subscriber

class CampaignAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','updated_at')
    search_fields = ('title','description')
    list_per_page = 1

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email','created_at','updated_at')
    search_fields = ('email',)
    list_per_page = 1


    

admin.site.register(Campaign,CampaignAdmin)
admin.site.register(Subscriber,SubscriberAdmin)

# Register your models here.
