from django.contrib import admin
from  .models import *

class ProfileAdmin(admin.ModelAdmin):
    # Cria um filtro de hierquia com datas
    data_hierarchy = 'created_at'
    #Elementos que desejamos que sejam listados
    list_display = ('user', 'role', 'birthday', 'specialtiesList', 'addressesList', )
    
    def specialtiesList(self, obj):
        return [i.name for i in obj.specialties.all() ]
    
    def addressesList(self, obj):
        return [i.name for i in obj.addresses.all()]
    list_display_links = ('user', 'role', )
    #Apresentação de campos vazios
    empty_value_display = 'Vazio'
    #Campos que poderam ser pesquisados
    search_fields = ('user__username', )
    
    fieldsets = (
        ('Usuário', {
            'fields': ('user', 'birthday', 'image')
        }),
        ('Função', {
            'fields': ('role', )
        }),
        
        ('Extras', {
            'fields': ('specialties', 'addresses')
        }),
    )
    
    def birth(self, obj):
        return obj.birthday
    birth.empty_value_display = '___/___/___'

    

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Province)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)






