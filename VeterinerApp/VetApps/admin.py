from django.contrib import admin
from VetApps.models import Customer,Kind,Animal

class CustomerAdmin(admin.ModelAdmin):
    list_display =['id','customerName','customerCity','customerPhone']
    class Meta:
        model = Customer

class AnimalAdmin(admin.ModelAdmin):
    list_display =['id','animalName','animalBirthdate','animalCustomer','animalKind']
    class Meta:
        model = Animal

class KindAdmin(admin.ModelAdmin):
    list_display =['id','kindName']
    class Meta:
        model = Kind

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Kind,KindAdmin)
admin.site.register(Animal,AnimalAdmin)
# Register your models here.
