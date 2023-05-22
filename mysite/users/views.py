#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib import messages
from .forms import UserEditForm
from .models import User
from django.contrib.auth.decorators import login_required


def main(request):
    return render(request,'users/main.html')
    

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request,'users/main.html')
        else:
            # 폼 유효성 검사에 실패한 경우, 오류 메시지를 messages 프레임워크를 사용해 전달
            messages.error(request, 'There was an error creating your account. Please check the form and try again.')
    else:
        form = CustomUserCreationForm()

    context = {'form': form}
    return render(request, 'users/signup.html', context)


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'users/profile.html', {'user': user})


@login_required
def edit_profile(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('users:profile', username=username)
    else:
        form = UserEditForm(instance=user)

    return render(request, 'users/edit_profile.html', {'form': form})