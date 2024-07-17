from django.contrib import admin

from businness import models


# criando adminn de Businnes
class BusinnessAdmin(admin.ModelAdmin):
    list_filter = ("is_active",)


# registar no admin do dajngo
admin.site.register(models.Businness, BusinnessAdmin)
