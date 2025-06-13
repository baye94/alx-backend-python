from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User

@login_required
def delete_user(request):
    user = request.user
    logout(request)
    user.delete()  # Triggers post_delete signal
    return redirect('home')

@login_required
def delete_user(request):
    """
    Deletes the currently logged-in user and logs them out.
    Automatically triggers post_delete signal to clean up related data.
    """
    user = request.user
    logout(request)
    user.delete()  # This will trigger post_delete signal
    return redirect('home')  # Adjust 'home' to your actual homepage route