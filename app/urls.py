from django.urls import path, re_path
from .views import home,comuncom,delete,update,registerpage,loginpage


urlpatterns = [
    path('',home),
    path('complate/<int:id>/',comuncom),
    path('delete/<int:id>/',delete),
    path('update/<int:id>/',update),
    path('register',registerpage,name='register'),
    path('login',loginpage,name='login')
]