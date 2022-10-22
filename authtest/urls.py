from django.urls import path
from authtest import views


urlpatterns = [
    path('login/', views.login_user, name='authtest_login'),
    path('register_student/', views.registration_student, name='authtest_register_student'),
    path('register_worker/', views.registration_worker, name='authtest_register_worker'),
    path('register/', views.register, name='authtest_register'),
    path('logout/', views.logout_user, name='authtest_logout'),
]




