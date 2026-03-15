from django.urls import path

from users.views import RegisterFormView, login_view, account_view, reset_password_view, verify_email_view

app_name = 'users'

urlpatterns = [
    path('register/', RegisterFormView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('account/', account_view, name='account'),
    path('reset-password/', reset_password_view, name='reset-password'),
    path('verify-email/<uidb64>/<token>/', verify_email_view, name='verify-email'),
]
