from django.urls import path
from . import views

urlpatterns = [
    ##path('', views.comments, name='comments'),
    # path('check-spam', views.check_spam, name='check_spam'),
    path('check', views.check, name='check'),
    # path('comments/<int:pk>/', views.delete_comment, name='delete-comment'),
   
   
    path('', views.home, name="home"),
    path('signup',views.signup, name ="signup"),
    path('signin',views.signin, name ="signin"),
    path('signout',views.signout, name ="signout"),
]