from django.views.generic import View 
from django.http import JsonResponse

class BlogsView(View):
    def get(self, request):
        res = {
            'success': True,
            'messsge': 'Class based view: api to get blogs'
        }
        return JsonResponse(res)

    def post(self, request, *args, **kwargs):
        res = {
            'success': True,
            'messsge': 'Class based view: api to create a blog'
        }
        return JsonResponse(res)

    def put(self, request, *args, **kwargs):
        res = {
            'success': True,
            'messsge': 'Class based view: api to update a blog'
        }
        return JsonResponse(res)

    def delete(self, request, *args, **kwargs):
        res = {
            'success': True,
            'messsge': 'Class based view: api to delete a blog'
        }
        return JsonResponse(res)