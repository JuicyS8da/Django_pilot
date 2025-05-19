from django.urls import path
from .views import profile, index, settings, test_result, contacts, subscribtions, ab_initio, news, about_us, games, memory_test, multitasking_test, basic_coordination_test

urlpatterns = [
    path('', index, name='index'),
    path('profile/', profile, name='profile'),
    path('settings/', settings, name='settings'),
    path('test_result/', test_result, name='test_result'),
    path('contacts/', contacts, name='contacts'),
    path('subscribtions/', subscribtions, name='subscribtions'),
    path('ab_initio/', ab_initio, name='ab_initio'),
    path('news/', news, name='news'),
    path('about_us/', about_us, name='about_us'),
    path('games/', games, name='games'),
    path('memory_test/', memory_test, name='memory_test'),
    path('multitasking_test/', multitasking_test, name='multitasking_test'),
    path('basic_coordination_test/', basic_coordination_test, name='basic_coordination_test'),
]