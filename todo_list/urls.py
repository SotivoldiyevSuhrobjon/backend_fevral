from django.urls import path
from . import views


urlpatterns = [
    path('', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    
    path('card_list/', views.card_list, name='card_list'),
    path('create_card/', views.create_card, name='create_card'),
    # path('task/', views.create_task, name='create_task'),
    # path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
    path('detail_btn/<int:pk>/', views.detail_btn, name='detail_btn'),
]