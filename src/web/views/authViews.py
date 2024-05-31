
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

from forms.auth_form import LoginForm

def gym_login(request):
    data = {}
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            inputs = form.cleaned_data
            user = authenticate(request, username=inputs.get('email_or_contact'), password=inputs.get('password'))
            if user:
                login(request, user=user)
                return redirect('/')
        form._errors['error'] = "Idendifiant incorrect"
    else:
        form = LoginForm()
    data['form'] = form
    print(form.errors)
    return render(request, 'account/login.html', context=data)

@login_required(login_url=settings.LOGIN_URL)
def gym_logout(request):
    logout(request)
    return redirect('/login')