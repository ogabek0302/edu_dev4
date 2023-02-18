from django.contrib import admin
from .models import Academy, Teacher, Course, Group, Student, Mark


class AcademyAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


class MarkAdmin(admin.ModelAdmin):
    list_display = ['student', 'reyting', 'mark', 'created_at']


admin.site.register(Mark, MarkAdmin)
admin.site.register(Academy, AcademyAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Group, GroupAdmin)
