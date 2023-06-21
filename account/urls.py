from django.urls import path, include

from django.contrib.auth.views import LoginView, LogoutView

from .views import register, edit_profile



urlpatterns = [
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout')
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('change_profile', edit_profile, name='change_profile')
]
