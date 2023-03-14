from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    # path('<int:pk>/', views.single_post_page), # localhost:8000/blog/1,2,3...
    # path('', views.index),  # ''는 localhost:8000/에 해당
]