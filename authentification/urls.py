from django.urls import path
from authentification import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register_student/', views.registration_student, name='register_student'),
    path('register_teacher/', views.registration_teacher, name='register_teacher'),
    path('register_worker/', views.registration_worker, name='register_worker'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
]
