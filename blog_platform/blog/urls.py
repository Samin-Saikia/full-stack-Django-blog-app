from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # HOME
    path('', views.home, name='home'),

    # CREATE / ADMIN ACTIONS (MUST BE FIRST)
    path('post/create/', views.create_post, name='create_post'),
    path('post/edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),

    # FILTERS
    path('category/<slug:slug>/', views.category_posts, name='category_posts'),
    path('tag/<int:tag_id>/', views.tag_posts, name='tag_posts'),

    # POST DETAIL (ALWAYS LAST)
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('my-posts/', views.my_posts, name='my_posts'),

]
