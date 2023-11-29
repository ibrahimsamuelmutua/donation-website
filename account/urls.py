from django.urls import path
from . import views as sam

urlpatterns = [
    path('register/', sam.register, name='register-url'),
    path('login/', sam.loginuser, name='login-url'),
    path('logout/', sam.log_out, name='logout-url'),
    path('member_profile/<int:id>/', sam.member_profile, name='member-profile-url')
]
