from django.urls import path
from . import views

urlpatterns=[

    path('',views.login,name="login"),
   
    path('register',views.register,name="register"),
    #path('index',views.index,name="index"),
     path('addstudent',views.addstudent,name="addstudent"),
     path('addfaculty',views.addfaculty,name="addfaculty"),
    # path('index_others',views.index_others,name="index_others")
    # path('get_sf_ratio',views.get_sf_ratio,name="get_sf_ratio")
  # path('Auth_Register',views.Auth_Register,name="Auth_Register"),
   # path('Stud_Register',views.Stud_Register,name="Stud_Register"),
]