from django.contrib import admin
from first_app.models import StudentModel, Course
# Register your models here.


@admin.register(StudentModel)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll']


@admin.register(Course)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ['cid', 'name', 'marks']
