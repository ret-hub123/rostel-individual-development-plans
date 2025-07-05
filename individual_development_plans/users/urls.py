from django.contrib.auth.views import LogoutView
from django.urls import path
from users.views import LoginUser, UsersCreate

app_name  = "users"

urlpatterns = [
    path('login/', LoginUser.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page='users:login') , name = 'logout'),
    path('registration/', UsersCreate.as_view(), name = 'registration'),
]
