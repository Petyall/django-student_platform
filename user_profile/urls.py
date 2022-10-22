from django.urls import path
from user_profile import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('download/', views.download_file, name='download_file'),
    path('parsed_page/', views.parsed_page, name='parsed_page'),
]