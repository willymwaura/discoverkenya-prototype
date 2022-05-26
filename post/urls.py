from django.urls import path
from. import views

urlpatterns=[

    path('all',views.index,name='index'),
    path('post/<str:pk>',views.posts,name='posts'),
    path('addexperience/<str:pk>',views.addexperience,name='addexperience'),
    path('',views.test,name='test'),
    path('perregion',views.perregion,name='perregion'),
    path('addfeature',views.addfeature,name='addfeature'),
    path('map', views.calculate_distance_view, name='calaculate-view'),

    ]