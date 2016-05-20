from django.contrib import admin
from .models import Members, Speaker, Conference, Assistant, Staff

# Register your models here.

admin.site.register(Members)
admin.site.register(Speaker)
admin.site.register(Conference)
admin.site.register(Assistant)
admin.site.register(Staff)
