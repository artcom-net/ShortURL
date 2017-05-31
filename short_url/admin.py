from django.contrib import admin

# Register your models here.
from .models import ShortURL


class ShortURLAdmin(admin.ModelAdmin):
    list_display = ['url', 'short_code', 'format_date', 'is_active']

    def format_date(self, obj):
        return obj.created.strftime('%d.%m.%Y in %H:%M')

    format_date.short_description = 'created'


admin.site.register(ShortURL, ShortURLAdmin)
