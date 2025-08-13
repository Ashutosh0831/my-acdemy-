
from django.db import models
from .models import Student, studentUser
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from mv_students.utils import hash_password 
from django.contrib.auth.backends import BaseBackend

class StudentBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            student = studentUser.objects.get(username=username)
            if student.check_password(password) and student.is_active:
                return student
        except studentUser.DoesNotExist:
            return None 
        
    def get_user(self, user_id):
        try:
            return studentUser.objects.get(pk=user_id)
        except studentUser.DoesNotExist:
            return None
        
        