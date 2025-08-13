from django.contrib import admin
from mv_students.models import Student, studentUser, StudentManager, StudentProfile

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 
                    'username', 
                    'email', 
                    'phone', 
                    'class_name', 
                    'school_name', 
                    'date_joined', 
                    'address',      
                    'father_name', 
                    'mother_name', 
                    'father_occupation', 
                    'mother_occupation', 
                    'father_number',
                    'password',
                    'profile_picture',
                    'date_of_birth')
    search_fields = ('name', 'username', 'email')
    list_filter = ('class_name', 'school_name')
    ordering = ('-date_joined',)
    list_per_page = 10

admin.site.site_header = "M.V. Academy Admin"
admin.site.site_title = "M.V. Academy Admin Portal"


class StudentUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    ordering = ('-username',)
    list_per_page = 10

admin.site.register(studentUser, StudentUserAdmin)  



@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'class_name', 'school_name', 'phone', 'father_name', 'mother_name', 'date_of_birth')
    search_fields = ('name', 'user__username', 'school_name')
    list_filter = ('class_name', 'gender')
    





