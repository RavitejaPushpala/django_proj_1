import json
from django.http import JsonResponse

def api_home(request,*args,**kwargs):
    print(request.GET) # used to get query params
    print(request.GET)

    data = {}
    try:
        data = json.loads(request.body)
    except:
        pass
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    data['params'] = dict(request.GET)
    return JsonResponse(data)