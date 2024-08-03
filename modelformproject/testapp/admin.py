from django.contrib import admin
from testapp.models import StudentModel
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','gmail','state','phonenumber','dob','gender']

admin.site.register(StudentModel,StudentAdmin)
