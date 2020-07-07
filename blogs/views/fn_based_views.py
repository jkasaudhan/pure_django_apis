from django.http import JsonResponse
import json

def get_blogs(request):
    res = {
        'success': True,
        'messsge': 'Function based view: api to get blogs'
    }
    return JsonResponse(res)

def create_blog(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        print(body.get('title'))
        res = {
            'success': True,
            'messsge': 'Function based view: api to create a blog'
        }
    else: 
        res = {
            'success': False,
            'messsge': 'Function based view: Invalid request'
        }
    return JsonResponse(res)

def update_blog(request):
    if request.method == 'PUT':
        res = {
            'success': True,
            'messsge': 'Function based view: api to update a blog'
        }
    else: 
        res = {
            'success': False,
            'messsge': 'Function based view: Invalid request'
        }
    return JsonResponse(res)