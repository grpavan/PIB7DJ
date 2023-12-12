from django .contrib import admin
from django .urls import path,re_path
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',views.home,name='home'),
    re_path(r'^list',views.list,name='list'),
    re_path(r'^create',views.create,name='create'),
    re_path(r'^edit', views.edit, name='edit'),
    re_path(r'^delete', views.delete, name='delete'),

]