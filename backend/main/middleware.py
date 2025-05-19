from django.shortcuts import redirect
from django.urls import resolve, reverse
import re

class LoginRequiredMiddleware:
    EXEMPT_URLS = [
        re.compile(r'^/$'),
        re.compile(r'^/login/?$'),
        re.compile(r'^/register/?$'),
        re.compile(r'^/admin/'),
        re.compile(r'^/static/'),
        # добавь сюда другие разрешённые URL при необходимости
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path_info

        if not request.user.is_authenticated:
            if not any(pattern.match(path) for pattern in self.EXEMPT_URLS):
                return redirect(reverse('login'))  # << фиксированный redirect сюда

        return self.get_response(request)
