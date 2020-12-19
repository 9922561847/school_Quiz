from django.urls import path

from quiz import views

urlpatterns = [
    path('',views.home,name="Reset"),
    path('test',views.test),
    path('answer',views.answer),
]