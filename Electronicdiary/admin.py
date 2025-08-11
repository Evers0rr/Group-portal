# from django.contrib import admin
# from .models import Student, Subjects, Grade
# from django.conf import settings
#
# from config import settings
#
# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('full_name', 'email', 'username')
#     search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')
#     ordering = ('user__last_name',)
#     autocomplete_fields = ('setting.AUTH_USER_MODEL',)
#
#     @admin.display(description="ПІБ")
#     def full_name(self, obj):
#         return f"{obj.user.first_name} {obj.user.last_name} "
#
#     @admin.display(description="Email")
#     def email(self, obj):
#         return obj.user.email
#
#     @admin.display(description="Логін")
#     def username(self, obj):
#         return obj.user.username
#
#
# @admin.register(Subjects)
# class SubjectsAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)
#     ordering = ('name',)
#
#
# @admin.register(Grade)
# class GradeAdmin(admin.ModelAdmin):
#     list_display = ('student_name', 'subject_name', 'value', 'date')
#     search_fields = ('student__user__username', 'student__user__last_name', 'subjects__name')
#     list_filter = ('date', 'subjects')
#     ordering = ('-date',)
#     autocomplete_fields = ('student', 'subjects')
#     list_select_related = ('student__user', 'subjects')
#
#     @admin.display(description="Студент")
#     def student_name(self, obj):
#         return f"{obj.student.user.first_name} {obj.student.user.last_name}"
#
#     @admin.display(description="Предмет")
#     def subject_name(self, obj):
#         return obj.subjects.name
#
