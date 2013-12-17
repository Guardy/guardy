from django.shortcuts import render
from django.shortcuts import redirect
from blog.models import Post
from lib.decorators import json_response
from django.template import Context
from django.template.loader import get_template
from datetime import datetime


def page(request, post):
    try:
        post = Post.objects.get(pk=int(post))
        return render(request, 'blog/page.html', locals())
    except:
        return redirect('/')


@json_response
def posts_range(request):
    try:
        if request.method == 'GET':
            post_from = datetime.strptime(request.GET['from'], '%Y-%m-%dT%H:%M:%S')
            count = int(request.GET['count'])
            preview = bool(request.GET.get('preview'))
            posts_list = Post.objects.filter(date_time__gt=post_from)
            tpl = get_template('blog/post.html')
            posts = []
            counter = 0
            has_more = False
            for post in posts_list:
                counter += 1
                if counter > count:
                    has_more = True
                    break
                posts.append({
                    'id': post.pk,
                    'datetime': post.date_time.isoformat(),
                    'html': tpl.render(Context(locals()))
                })
            error = None
            status = 200
            response = {'more': has_more,
                        'posts': posts,
                        'error': error,
                        'status': status}
        else:
            response = {'error': 'wrong method',
                        'status': 500}
        return response
    except Exception, exc:
        status = 500
        error = str(exc.args[0])
        return {'error': error,
                'status': status}