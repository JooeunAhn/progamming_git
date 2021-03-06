from django.conf import settings

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.contrib.auth import get_user_model, get_backends, authenticate, login as auth_login

from django.contrib.auth.tokens import default_token_generator as default_token_generator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode


from accounts.forms import SignupForm, SignupForm2
from accounts.forms import send_signup_confirm_email





"""
authenticated_user = authenticate(
    24
+                    username=form.cleaned_data['username'],
    25
+                    password=form.cleaned_data['password1'])
    26
+
    27
+            auth_login(request, authenticated_user)
"""


# Create your views here.
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm2(request.POST)
        if form.is_valid():

            user = form.save()
            authenticated_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'])
            auth_login(request, authenticated_user)

            #회원가입 승인
            #backend_cls = get_backends()[0].__class__
            #backend_path = backend_cls.__module__ + '.' + backend_cls.__name__
            #user.backend = backend_path
            #auth_login(request, user)

            messages.info(request, '환영합니다')
            return redirect(settings.LOGIN_REDIRECT_URL)

            #회원가입 시에, 이메일 승인
            #user = form.save(commit = False)
            #user.is_active = False ##user 에게 권한주는 것의 핵심
            #user.save()
            #send_signup_confirm_email(request, user)
            #return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm2()
    return render(request, 'accounts/signup.html',
        {'form': form,})

def signup_confirm(request,uidb64,token):

    User = get_user_model()

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk = uid)

    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.info(request, '인증확인')

        return redirect(settings.LOGIN_URL)
    else:
        messages.error(request, '잘못된경로임')
        return redirect(settings.LOGIN_URL)




