from django.contrib import admin

from modelstudy.models import School, Student, User, Role, Person, Comment

# Register your models here.

admin.site.register(School)
admin.site.register(Student)
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Person)
admin.site.register(Comment)