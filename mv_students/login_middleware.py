#mv_students/midddleware.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse

class BackLoginIfAuthenticatedMiddleware(MiddlewareMixin):
    def process_request(self, request):

        excluded_paths = [
            reverse('index'),
            reverse('user_login'),
            reverse('user_register'),
        ]

        if request.user.is_authenticated:
            if request.path in excluded_paths:
                # Redirect to the student dashboard if the user is authenticated
                return redirect('student_dashboard')
        else:
            # If the user is not authenticated, allow the request to proceed
            return None
        
        
