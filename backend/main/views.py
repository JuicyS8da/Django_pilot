from django.shortcuts import render

def profile(request):
    return render(request, 'main.html')

def index(request):
    return render(request, 'index.html')

def test_result(request):
    return render(request, 'test_result.html')

def settings(request):
    return render(request, 'settings.html')

def contacts(request):
    return render(request, 'contacts.html')

def subscribtions(request):
    return render(request, 'subscriptions.html')

def ab_initio(request):
    return render(request, 'ab_initio.html')

def news(request):
    return render(request, 'news.html')

def about_us(request):
    return render(request, 'about_us.html')

def games(request):
    return render(request, 'games.html')

def vlek(request):
    return render(request, 'vlek.html')

def memory_test(request):
    return render(request, 'short_memory_game.html')

def multitasking_test(request):
    return render(request, 'COMPASS - Multitasking.html')

def basic_coordination_test(request):
    return render(request, 'COMPASSBasic_coordination.html')