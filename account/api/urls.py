from django.urls import path
from account.api.views import registration_view, profile_view, profile_update_view, logout_view
from rest_framework.authtoken.views import obtain_auth_token
app_name = 'account'

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('profile/', profile_view, name='profile'),
    path('profile/update', profile_update_view, name='update'),
    path('logout/', logout_view, name='logout'),
]
