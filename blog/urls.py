from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name='home'),
    path('login',views.user_login,name='login'),
    path('logout',views.logout_view,name="logout"),
    path("registration",views.user_registration,name="registration"),
    path('list-post',views.list_posts,name='list-post'),
    path('create-post',views.create_post,name="create-post"),

    path('post/<int:post_id>/view/', views.view_post, name='view_post'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),

    path('add-comments/<int:id>/post',views.add_comment_post, name='add-comment-post')
]




