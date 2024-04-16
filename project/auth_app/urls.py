from django.urls import path
from .views import logout_view,login_view,change_pass,signup


urlpatterns = [
    path('signup/',signup,name='signup_url'),
    path('login/',login_view,name='login_url'),
    path('logout/',logout_view,name='logout_url'),
    path('change/',change_pass,name='change_url')
]