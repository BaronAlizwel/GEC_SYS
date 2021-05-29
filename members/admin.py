from django.contrib import admin
# , #CommitteeMembership
from .models import Member, Shepherd, Ministry, Group, Committee, Role
# from .models import Member, Shepherd, Ministry, Group, Committee, Role, MemberRole
# Register your models here.

admin.site.register(Ministry)
admin.site.register(Shepherd)
admin.site.register(Member)
admin.site.register(Group)
# admin.site.register(GroupMembership)
admin.site.register(Committee)
admin.site.register(Role)
# admin.site.register(MemberRole)
# admin.site.register(CommitteeMembership)
