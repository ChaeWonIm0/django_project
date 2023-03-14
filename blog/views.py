from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.
class PostList(ListView):
      model = Post

class PostDetail(DetailView):
     model = Post

# def index(request):
#     # posts = Post.objects.all() # 작성시간별 내림차순
#     posts = Post.objects.all().order_by('-pk') # 작성시간별 오름차순
#
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts' : posts,
#         }
#     )

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/post_detail.html',
#         {
#             'post' : post,
#         }
#     )