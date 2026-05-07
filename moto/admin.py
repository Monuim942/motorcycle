from django.contrib import admin
from .models import Admin,User

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','select_your_trip','phone_number','datetime')

    def __str__(self):
        return self.datetime
    
    search_fields = ['first_name',
        'last_name',
        'phone_number',
        'datetime__date',
        'datetime__time',]
    list_filter = ['datetime__date','datetime__time']
admin.site.register(Admin)
admin.site.register(User,UserAdmin)
admin.site.site_header = ' TOUR WITHDRAK '
admin.site.site_title = ' TOUR WITHDRAK '