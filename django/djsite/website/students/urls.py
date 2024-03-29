from django.urls import path
from students import views


urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("blog/", views.blog, name="blog"),
    path("login/", views.login, name="login"),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
]
