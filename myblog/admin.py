from django.contrib import admin
from .models import Blog, Comment
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Editable',{
            'fields': ('title', 'thumbnail', 'content', 'author')
        }),
        ('Non-Editable',{
            'fields': ('slug', 'number_of_reads'),
            'classes' : ('collapse',)
        })
    )
    readonly_fields = ('number_of_reads', 'slug') 

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)