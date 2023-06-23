from django.contrib import admin

from .models import Member, Group, Integrante, BelbinUserProfile

admin.site.register(Member)
admin.site.register(Group)
admin.site.register(Integrante)
admin.site.register(BelbinUserProfile)