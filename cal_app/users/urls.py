from django.urls import path
from users.views import UsernameCountView, Register, Login, index, addUser, showEditDialog, editUser, delete
urlpatterns = [
    # 判断用户名是否重复
    path('usernames/<username:username>/count/', UsernameCountView.as_view()),
    path('register/', Register),
    path('login/', Login),
    # path('logout/', LogoutView.as_view()),
    path('index/', index),
    path('add/', addUser),
    path('showEdit/<int:id>/', showEditDialog),
    path('edit/<int:uid>/', editUser),
    path('delete/<int:uid>/', delete),

]
