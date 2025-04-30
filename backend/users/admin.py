from django.contrib import admin
from .models import CustomUser, Subscription, UserSubscription

admin.site.register(CustomUser)
admin.site.register(Subscription)
admin.site.register(UserSubscription)
