from django.contrib import admin

from .models import Profile, Group, Member, BelbinUserProfile

admin.site.register(Profile)
admin.site.register(Group)
admin.site.register(Member)
admin.site.register(BelbinUserProfile)