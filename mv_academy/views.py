from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from mv_students.models import Student, studentUser, StudentProfile
from mv_students.utils import hash_password
from django.contrib.auth.hashers import check_password
from mv_students.authenticate import StudentBackend
from django.core.mail import send_mail
from django.utils.crypto import get_random_string





@login_required
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

@login_required
def main(request):
    return render(request, 'main.html')




@login_required
def logout_user(request):
    logout(request)
    request.session.flush()  # Clear the session data
    messages.success(request, "You have been logged out successfully.")

    return redirect('index')

def register_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        class_name = request.POST.get('class')
        school_name = request.POST.get('s_school')
        father_name = request.POST.get('f_name')
        mother_name = request.POST.get('m_name')
        date_of_birth = request.POST.get('dofb')
        father_occupation = request.POST.get('f_occupation')
        mother_occupation = request.POST.get('m_occupation')
        father_number = request.POST.get('f_number')
        username = request.POST.get('username')
        if Student.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose a different one.")
            return render(request, 'student_register.html') 
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')
        profile_picture = request.FILES.get('profile_picture')

        # Here you would typically save the student data to the database
        if password != c_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'student_register.html')
        
        #student User creation
        student_user = studentUser.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        student_user.save()

        # Create a StudentProfile instance
        student_profile = StudentProfile.objects.create(
            user=student_user,
            name=name,
            phone=phone,
            father_name=father_name,
            mother_name=mother_name,
            address=address,
            class_name=class_name,
            school_name=school_name,
            date_of_birth=date_of_birth,
        )
        student_profile.profile_picture = profile_picture
        student_profile.save()

        
        # Assuming you have a Student model to save the data
        rd = Student(
            name=name,
            email=email,
            phone=phone,
            gender=gender,
            address=address,
            class_name=class_name,
            school_name=school_name,
            father_name=father_name,
            mother_name=mother_name,
            date_of_birth=date_of_birth,
            father_occupation=father_occupation,
            mother_occupation=mother_occupation,
            father_number=father_number,
            username=username,
            password=password,
            profile_picture=profile_picture
        )
        try:
            rd.save()
            messages.success(request, "Registration successful!")
            return redirect('user_login')
        except Exception as e:
            messages.error(request, f"Registration failed: {e}")
            return render(request, 'student_register.html') 
    else:
        return render(request, 'student_register.html')

def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['student_id'] = user.id
            messages.success(request, "Login successful!")
            return redirect('main')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'student_login.html')

    return render(request, 'student_login.html')


def index(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'about_us.html')


def contactus(request):
    return render(request, 'contact_us.html')

def gallery(request):
    return render(request, 'gallery.html')


def reset_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'reset_password.html')
        try:
            user = studentUser.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            messages.success(request, "Password reset successful. Please log in with your new password.")
            return redirect('user_login')
        except studentUser.DoesNotExist:
            messages.error(request, "Username does not exist.")
            return render(request, 'reset_password.html')
    else:
        return render(request, 'reset_password.html')