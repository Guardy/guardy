from django import template

register = template.Library()


def app_name(app_name_value):
    try:
        app = __import__(app_name_value.lower())
        return app.app_label
    except:
        return app_name_value


register.simple_tag(app_name)

