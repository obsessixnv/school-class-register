from django import forms
from .models import Student, StudentInfo

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name_student', 'id_class']

class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['email', 'phone_field', 'birth_date']

from .models import TeacherInfo, Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['id_teacher', 'full_name_teacher']

class TeacherInfoForm(forms.ModelForm):
    class Meta:
        model = TeacherInfo
        fields = ['email', 'phone_field', 'birth_date', 'teacher_discipline', 'teacher_class']


class GradeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        disciplines = kwargs.pop('disciplines')
        super(GradeForm, self).__init__(*args, **kwargs)
        for discipline in disciplines:
            self.fields['1_sem_grade_' + str(discipline.id_discipline)] = forms.IntegerField(label=discipline.discipline_name + ' - 1st Semester Grade', required=False)
            self.fields['2_sem_grade_' + str(discipline.id_discipline)] = forms.IntegerField(label=discipline.discipline_name + ' - 2nd Semester Grade', required=False)
            self.fields['final_grade_' + str(discipline.id_discipline)] = forms.IntegerField(label=discipline.discipline_name + ' - Final Grade', required=False)