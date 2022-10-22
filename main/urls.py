from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('auth/', include('authtest.urls')),
    path('blog/', include('blog.urls')),
    path('profile/', include('user_profile.urls')),
]
