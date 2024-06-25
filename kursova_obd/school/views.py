from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponseRedirect
from .models import Student, Discipline
from django.shortcuts import render, redirect
from .forms import StudentForm, StudentInfoForm, GradeForm
from .models import Teacher
def teachers_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'school/teachers.html', {'teachers': teachers})

def add_student(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        student_info_form = StudentInfoForm(request.POST)
        if student_form.is_valid() and student_info_form.is_valid():
            student = student_form.save()
            student_info = student_info_form.save(commit=False)
            student_info.id_student = student
            student_info.save()
            return redirect('home')  # Повертаємо користувача на головну сторінку після успішного додавання
    else:
        student_form = StudentForm()
        student_info_form = StudentInfoForm()
    return render(request, 'school/add_student.html', {'student_form': student_form, 'student_info_form': student_info_form})
def get_students_data(request):
    students = Student.objects.all() # Отримайте всіх студентів з бази даних
    students_data = [{'full_name_student': student.full_name_student, 'class_name': student.id_class.class_name, 'email': student.studentinfo.email, 'phone_number': student.studentinfo.phone_field, 'birth_date': student.studentinfo.birth_date} for student in students]
    return JsonResponse(students_data, safe=False)
def delete_student(request, student_id):
    if request.method == 'POST':
        student = Student.objects.get(id_student=student_id)
        student.delete()
    return redirect('students')


from .forms import TeacherForm, TeacherInfoForm

def add_teacher(request):
    if request.method == 'POST':
        teacher_form = TeacherForm(request.POST)
        teacher_info_form = TeacherInfoForm(request.POST)
        if teacher_form.is_valid() and teacher_info_form.is_valid():
            teacher = teacher_form.save()  # Зберігаємо дані про вчителя
            teacher_info = teacher_info_form.save(commit=False)  # Створюємо об'єкт TeacherInfo, але ще не зберігаємо в базі даних
            teacher_info.id_teacher = teacher  # Прив'язуємо об'єкт TeacherInfo до вчителя
            teacher_info.save()  # Зберігаємо дані про вчителя в базі даних
            return redirect('teachers_list')  # Перенаправляємо користувача на сторінку зі списком вчителів
    else:
        teacher_form = TeacherForm()
        teacher_info_form = TeacherInfoForm()
    return render(request, 'school/add_teacher.html', {'teacher_form': teacher_form, 'teacher_info_form': teacher_info_form})

def delete_teacher(request, teacher_id):
    if request.method == 'POST':
        teacher = Teacher.objects.get(id_teacher=teacher_id)
        teacher.delete()
    # Після видалення перенаправте користувача на сторінку зі списком вчителів
    return redirect('teachers_list')
def students_view(request):
    # Отримайте список студентів
    students = Student.objects.all()

    # Передайте список студентів у шаблон для відображення
    return render(request, 'school/students.html', {'students': students})
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'school/login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'school/login.html')

# views.py
from django.shortcuts import render, get_object_or_404
from .models import Class, Student, Grade

def class_list(request):
    classes = Class.objects.all()
    return render(request, 'school/class_list.html', {'classes': classes})

def class_detail(request, class_id):
    students = Student.objects.filter(id_class=class_id)
    return render(request, 'school/class_detail.html', {'students': students})

from django.http import HttpResponseRedirect

from .forms import GradeForm  # Імпортуємо форму

def student_detail(request, student_id):
    student = get_object_or_404(Student, id_student=student_id)
    disciplines = Discipline.objects.all()
    grades = Grade.objects.filter(id_student=student_id)

    if request.method == 'POST':
        form = GradeForm(request.POST, disciplines=disciplines)
        if form.is_valid():
            for discipline in disciplines:
                grade_1_sem = form.cleaned_data.get('1_sem_grade_' + str(discipline.id_discipline))
                grade_2_sem = form.cleaned_data.get('2_sem_grade_' + str(discipline.id_discipline))
                final_grade = form.cleaned_data.get('final_grade_' + str(discipline.id_discipline))

                Grade.objects.update_or_create(
                    id_student=student,
                    id_discipline=discipline,
                    defaults={
                        'number_1_sem_grade': grade_1_sem,
                        'number_2_sem_grade': grade_2_sem,
                        'final_grade': final_grade,
                    }
                )
            return HttpResponseRedirect('/student/' + str(student_id) + '/')
    else:
        form = GradeForm(disciplines=disciplines)


    grade_list = []
    for discipline in disciplines:
        try:
            grade = grades.get(id_discipline=discipline)
            grade_list.append(grade)
        except Grade.DoesNotExist:
            grade_list.append(Grade(id_student=student, id_discipline=discipline, number_1_sem_grade=0, number_2_sem_grade=0, final_grade=0))

    return render(request, 'school/student_detail.html', {'student': student, 'grades': grades, 'disciplines': disciplines, 'grade_list': grade_list, 'form': form})




def home(request):
    return render(request, 'school/main.html')