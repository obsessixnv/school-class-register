from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    id_account = models.AutoField(primary_key=True)
    login = models.CharField(max_length=45)
    password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'account'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Class(models.Model):
    id_class = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=5)
    id_teacher = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='id_teacher')

    class Meta:
        managed = False
        db_table = 'class'
    def __str__(self):
        return self.class_name


class Discipline(models.Model):
    id_discipline = models.AutoField(primary_key=True)
    discipline_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'discipline'
    def __str__(self):
        return self.discipline_name

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Grade(models.Model):
    id_grade = models.AutoField(primary_key=True)
    number_1_sem_grade = models.IntegerField(db_column='1_sem_grade')  # Field renamed because it wasn't a valid Python identifier.
    number_2_sem_grade = models.IntegerField(db_column='2_sem_grade')  # Field renamed because it wasn't a valid Python identifier.
    final_grade = models.IntegerField()
    id_student = models.ForeignKey('Student', models.DO_NOTHING, db_column='id_student')
    id_discipline = models.ForeignKey(Discipline, models.DO_NOTHING, db_column='id_discipline')

    class Meta:
        managed = False
        db_table = 'grade'


class Principal(models.Model):
    id_principal = models.BigAutoField(primary_key=True)
    full_name_principal = models.CharField(max_length=45)
    id_principal_info = models.ForeignKey('PrincipalInfo', models.DO_NOTHING, db_column='id_principal_info')
    id_account = models.ForeignKey(Account, models.DO_NOTHING, db_column='id_account')

    class Meta:
        managed = False
        db_table = 'principal'


class PrincipalInfo(models.Model):
    id_principal_info = models.AutoField(primary_key=True)
    email = models.CharField(max_length=45)
    adress = models.CharField(max_length=45)
    phone_field = models.IntegerField(db_column='phone_№')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    birth_date = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'principal_info'


class Student(models.Model):
    id_student = models.AutoField(primary_key=True)
    full_name_student = models.CharField(max_length=45)
    id_class = models.ForeignKey(Class, models.DO_NOTHING, db_column='id_class')

    class Meta:
        managed = False
        db_table = 'student'


class StudentInfo(models.Model):
    id_student = models.OneToOneField(Student, models.DO_NOTHING, db_column='id_student', primary_key=True)
    email = models.CharField(max_length=45)
    phone_field = models.CharField(db_column='phone_№', max_length=18)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    birth_date = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'student_info'


class Teacher(models.Model):
    id_teacher = models.AutoField(primary_key=True)
    full_name_teacher = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'teacher'



class TeacherInfo(models.Model):
    id_teacher = models.OneToOneField(Teacher, models.DO_NOTHING, db_column='id_teacher', primary_key=True)
    email = models.CharField(max_length=45)
    phone_field = models.CharField(db_column='phone_№', max_length=15)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    birth_date = models.CharField(max_length=10)
    teacher_discipline = models.ForeignKey(Discipline, models.DO_NOTHING, db_column='teacher_discipline')
    teacher_class = models.ForeignKey(Class, models.DO_NOTHING, db_column='teacher_class')

    class Meta:
        managed = False
        db_table = 'teacher_info'
