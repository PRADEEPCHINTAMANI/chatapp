from django.urls import path
from . import views
urlpatterns = [
    # URL form : "/api/messages/1/2"
    path('chat', views.message_list, name='message-detail'),  # For GET request.
    # URL form : "/api/messages/"
    path('api/messages/', views.message_list, name='message-list'),   # For POST
    # URL form "/api/users/1"
    path('api/users/<int:pk>', views.user_list, name='user-detail'),      # GET request for user with id
    path('api/users/', views.user_list, name='user-list'),    # POST for new user and GET for all users list
       path('', views.index1, name='index1'),
       path('register', views.register_view, name='register'),
]