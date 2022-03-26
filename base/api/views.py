from django.http import JsonResponse

def getRoutes(request):
    routes = [
        'Get /api/rooms',
        'Get /api/:id'
    ]
    return JsonResponse(routes, safe=False)