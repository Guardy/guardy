from django.contrib import admin
from home.models import Article
from blog.models import Author, Post
from software.models import Program

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Program)
