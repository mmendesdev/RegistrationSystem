from businness import models
from django.contrib import admin


#criando adminn de Businnes 
class BusinnessAdmin(admin.ModelAdmin):
     list_filter = ('is_active',)

#registar no admin do dajngo
admin.site.register(models.Businness, BusinnessAdmin)