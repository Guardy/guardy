import json
from django.http import HttpResponse
from django.views.decorators.cache import add_never_cache_headers



def json_response(func):
    """
    A decorator thats takes a view response and turns it
    into json. If a callback is added through GET or POST
    the response is JSONP.
    """
    def decorator(*args, **kwargs):
        try:
            REQUEST = args[0].REQUEST
        except:
            REQUEST = args[1].REQUEST
        objects = func(*args, **kwargs)
        if isinstance(objects, HttpResponse):
            return objects
        try:
            data = json.dumps(objects)
            if 'callback' in REQUEST:
                # a JSONP response!
                data = '%s(%s);' % (REQUEST['callback'], data)
                return HttpResponse(data, "text/javascript")
        except:
            data = json.dumps(str(objects))
        response = HttpResponse(data, "application/json")
        add_never_cache_headers(response)
        return response

    return decorator