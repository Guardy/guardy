from django.shortcuts import render
from home.models import Article
from blog.models import Post
from django.http import Http404


def page(request, page_no=0):
    # try:
        preview = True
        articles = Article.objects.all()
        posts = Post.objects.all()
        show_more_count = 3
        first_blog_post = int(page_no) * show_more_count
        last_blog_post = first_blog_post + show_more_count
        has_more = last_blog_post < posts.count()
        next_page = int(page_no) + 1
        return render(request, 'home/page.html', locals())
    # except:
    #     raise Http404
