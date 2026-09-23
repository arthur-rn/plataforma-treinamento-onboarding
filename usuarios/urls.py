from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('<slug:slug>/login/', views.login_empresa_view, name='login'),
    path('<slug:slug>/logout/', views.logout_empresa_view, name='logout'),
    path('<slug:slug>/', views.dashboard_empresa_view, name='dashboard'),
]