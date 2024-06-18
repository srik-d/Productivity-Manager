from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from ToDo.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'complete', 'create')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user=request.user)

admin.site.register(Task, TaskAdmin)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
