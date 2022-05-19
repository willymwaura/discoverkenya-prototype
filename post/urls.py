from django.urls import path
from. import views

urlpatterns=[

    path('',views.index,name='index'),
    path('post/<str:pk>',views.posts,name='posts'),
    path('addexperience/<str:pk>',views.addexperience,name='addexperience'),
    path('test',views.test,name='test'),
    path('perregion',views.perregion,name='perregion'),
    path('addfeature',views.addfeature,name='addfeature')
    ]