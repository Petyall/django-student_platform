from django.urls import path
from authtest import views

# urlpatterns = [
#     path('reg/', views.registration_student, name='reg'),
#     path('login/', views.login_user, name='reg'),
#     path('logout/', views.logout_user, name='reg'),
# ]


urlpatterns = [
    path('login/', views.login_user, name='authtest_login'),
    path('register_student/', views.registration_student, name='authtest_register_student'),
    # path('register_teacher/', views.registration_teacher, name='register_teacher'),
    # path('register_worker/', views.registration_worker, name='register_worker'),
    path('register/', views.register, name='authtest_register'),
    path('logout/', views.logout_user, name='authtest_logout'),
]




