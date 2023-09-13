from django.urls import path,include
from bank_app import views

urlpatterns = [
    path('',views.dmo,name="dmo"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('apply/',views.apply,name="apply"),
    path('logout/',views.logout,name="logout")
]
