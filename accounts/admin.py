from django.contrib import admin

from accounts.models import Gender, User, Trainer

# Register your models here.

admin.site.register(Gender)
admin.site.register(User)
admin.site.register(Trainer)
