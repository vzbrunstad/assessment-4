from django.urls import path

from . import views

app_name = 'craigslist'

urlpatterns = [
    path('', views.home, name = 'home' ),# /categories: A page listing all the categories
    path('new/', views.category_new, name = 'category_new'),# /categories/new: A page with a form to create a new category
    path('<int:category_id>/', views.category_detail, name='category_detail'),# /categories/:category_id: A page to view the detail of a specific category and a list of all of its associated posts
    path('<int:category_id>/edit', views.category_edit, name='category_edit'),# /categories/:category_id/edit: A page with a form to update a specific category, with current values filled in already. Also include the ability to delete the specific category here.
    path('<int:category_id>/delete', views.category_delete, name='category_delete'),# /categories/:category_id/delete: A page with a form to update a specific category, with current values filled in already. Also include the ability to delete the specific category here.

    path('<int:category_id>/posts/new/', views.post_new, name = 'post_new'),# /categories/:category_id/posts/new: A page with a form to create a new post, under the current category by default.
    path('<int:category_id>/posts/<int:post_id>', views.post_show, name='post_show'),# /categories/:category_id/posts/:post_id: A page to view the detail of a specific post. Also include the ability go back to the parent category detail page (/categories/:category_id/)

    path('<int:category_id>/posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),# /categories/:category_id/posts/:post_id/edit: A page with a form to update a specific post, with current values filled in already. Also include the ability to delete the specific post here.

    path('<int:category_id>/posts/<int:post_id>/delete/', views.post_delete, name='post_delete'),# /categories/:category_id/posts/:post_id/delete: A page with a form to update a specific post, with current values filled in already. Also include the ability to delete the specific post here.
]







