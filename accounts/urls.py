from django.urls import path
from .views import *
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', home, name='home'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('register', register, name='register'),
    path('dashboard', dashboard, name='dashboard'),
    
     # when user logged in.
    path('password_change/', PasswordChangeView.as_view(template_name="change/password_change_form.html"), name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(template_name="change/password_change_done.html"), name='password_change_done'),
    
    # when user forgot password
    path('password_reset/', PasswordResetView.as_view(template_name="change/password_reset.html"), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name="change/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="change/set_new_password.html"), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name="change/password_reset_complete.html"), name='password_reset_complete'),
    

]
