from . import views
from django.urls import path, include
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('exit/', authViews.LogoutView.as_view(template_name='school/exit.html'), name='logout'),
    path('students/', views.students_view, name='students'),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('teachers/delete/<int:teacher_id>/', views.delete_teacher, name='delete_teacher'),
    path('students_data/', views.get_students_data, name='students_data'),
    path('add_student/', views.add_student, name='add_student'),
    path('teachers/', views.teachers_list, name='teachers_list'),
    path('teachers/add/', views.add_teacher, name='add_teacher'),
    path('classes/', views.class_list, name='class_list'),
    path('class/<int:class_id>/', views.class_detail, name='class_detail'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
]
