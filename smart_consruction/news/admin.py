from django.contrib import admin
from .models import PostNews


class PostNewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'heading', 'text', 'pub_date', 'image',)
    list_editable = ('heading', 'text', 'image')
    search_fields = ('heading', 'text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(PostNews, PostNewsAdmin)
