from django.urls import path
from. import views

urlpatterns=[

    path('',views.index,name='index'),
    path('post/<str:pk>',views.posts,name='posts'),
    path('addexperience/<str:pk>',views.addexperience,name='addexperience')
    ]