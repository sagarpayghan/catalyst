from django.urls import path,include
from . import views
urlpatterns = [
    path('querydata/',views.query_view,name='querypage'),
    path('users/',views.user_view,name='userspage'),
    path('create/',views.create_user,name='createpage'),
    path('delete/<int:id>',views.delete_user,name='deleteuser'),
    path('',views.upload_view,name='uploadpage'),
    path('get/',views.getData,name='getpage'),
    path('post/',views.postData,name='postpage'),
    
]