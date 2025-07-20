from django.contrib import admin

from skilltracker.models import Tasks, Comments


# Register your models here.


@admin.register(Tasks)
class UserAdmin(admin.ModelAdmin):
    list_display = ('title', 'employee')


@admin.register(Comments)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id',)
