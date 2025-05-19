from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomRegisterForm, CustomAuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        print('Data from login came')
        print(form.errors)
        print(request.POST)
        if form.is_valid():
            print("Form is valid")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            print(form.errors)
            if user is not None:
                print("User is authenticated")
                login(request, user)
                return redirect('profile')
        else:
            print(form.errors)
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', context={'form': form})

def register_view(request):
    errors = []  # сюда соберём все ошибки

    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print("Форма валидна")
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            # Собираем все ошибки формы
            for field, field_errors in form.errors.items():
                for error in field_errors:
                    errors.append(error)
    else:
        form = CustomRegisterForm()

    context = {
        'form': form,
        'errors': errors,
    }
    return render(request, 'registration.html', context)


def sign_out(request):
    logout(request)
    return redirect('login')