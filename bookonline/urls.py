from django.urls import path, include
from . import views
from .views import *


urlpatterns = [
   
    
    #path('about/', views.about, name='babout'),
    
    
    path('', views.home, name='bhome'), 
    
    path('home2/', views.home2, name='bhome2'), 
     

    
    
    path('<int:bookid>/<str:chptitle>/<int:sub1>/<int:sub2>', views.sub2display, name="sub2display"),
    path('<int:bookid>/<str:chptitle>/<int:sub1>', views.sub1display, name="sub1display"),
    path('<int:bookid>/<str:chptitle>', views.chapterdisplay, name="chapterdisplay"),
    path('booklist/', views.booklist, name="booklist"),
    
    # path('<int:bookid>/', views.bookid, name="bookid"),
    path('<int:bookid>/', views.books, name="books"),
    path('index/<int:pk>', views.index, name="index"),
    path('<int:bookid>/<str:subhead>', views.titles, name="titles"),
    

    path('findex/', views.findex, name="findex"),
   



    






]
 