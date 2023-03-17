from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView, DetailView

# 블로그 메인 글 리스트
class PostList(ListView):
      model = Post
      def get_context_data(self, **kwargs):
          context = super(PostList, self).get_context_data()
          context['categories'] = Category.objects.all()
          context['no_category_post_count'] = Post.objects.filter(category=None).count()
          return context

# 블로그 글 상세페이지
class PostDetail(DetailView):
     model = Post
     def get_context_data(self, **kwargs):
         context = super(PostDetail, self).get_context_data()
         context['categories'] = Category.objects.all()
         context['no_category_post_count'] = Post.objects.filter(category=None).count()
         return context

# 블로그 카테고리 페이지

def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)
    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'category': category,
        }
    )

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