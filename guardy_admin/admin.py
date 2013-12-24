from django.contrib import admin
from home.models import Article
from blog.models import Author, Post
from software.models import Program
from django import forms
from software import refresher
import inspect


def refresh_functions():
    functions = inspect.getmembers(refresher, inspect.isfunction)
    choices = tuple([(func[0], func[0]) for func in functions])
    return choices


class DynamicChoiceField(forms.ChoiceField):
    def valid_value(self, value):
        return True


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program

    def __init__(self, *args, **kwargs):
        super(ProgramForm, self).__init__(*args, **kwargs)
        self.fields['refresh_function_name'] = DynamicChoiceField(choices=refresh_functions())

class ProgramAdmin(admin.ModelAdmin):
    """
    customization Program model admin
    """
    form = ProgramForm


admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Program, ProgramAdmin)
