from django.contrib import admin
from django.urls import path, include
from todolist_app import views as todolist_app_views

urlpatterns = [
    path('', todolist_app_views.index, name='index'),
    path('admin/', admin.site.urls),
    path('todolist/', include('todolist_app.urls')),
    path('account/', include('users_app.urls')),
    path('about/', todolist_app_views.about, name='about'),
]
