from django.contrib import admin
from django.contrib import admin
from .models import Account, AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, Class, Discipline, DjangoAdminLog, DjangoContentType, DjangoMigrations, DjangoSession, Grade, Principal, PrincipalInfo, Student, Teacher, StudentInfo, TeacherInfo

admin.site.register(Account)
admin.site.register(AuthGroup)
admin.site.register(AuthGroupPermissions)
admin.site.register(AuthPermission)
admin.site.register(AuthUser)
admin.site.register(AuthUserGroups)
admin.site.register(AuthUserUserPermissions)
admin.site.register(Class)
admin.site.register(Discipline)
admin.site.register(DjangoAdminLog)
admin.site.register(DjangoContentType)
admin.site.register(DjangoMigrations)
admin.site.register(DjangoSession)
admin.site.register(Grade)
admin.site.register(Principal)
admin.site.register(PrincipalInfo)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(StudentInfo)
admin.site.register(TeacherInfo)

# Register your models here.
