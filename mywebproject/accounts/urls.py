from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('articles/', views.articles, name='articles'),
    path('create_article/', views.create_article, name='create_article'),
    #path('register/', views.register, name='register'),
]