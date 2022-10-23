from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sience', views.sience, name='sience'),
    path('profsouz', views.profsouz, name='profsouz'),
    path('studsovet', views.studsovet, name='studsovet'),
    path('admin/', admin.site.urls),
    path('auth/', include('authtest.urls')),
    path('blog/', include('blog.urls')),
    path('profile/', include('user_profile.urls')),
]
