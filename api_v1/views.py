import json

from django.http import JsonResponse


# Create your views here.


def add_view(request):
    body = json.loads(request.body)
    a = body.get('A')
    b = body.get('B')
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return JsonResponse({'error': "Type by not int"}, status=400)
    answer = a + b
    return JsonResponse({'answer': answer})


def subtract_view(request):
    body = json.loads(request.body)
    a = body.get('A')
    b = body.get('B')
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return JsonResponse({'error': "Type by not int"}, status=400)
    answer = a - b
    return JsonResponse({'answer': answer})


def multiply_view(request):
    body = json.loads(request.body)
    a = body.get('A')
    b = body.get('B')
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return JsonResponse({'error': "Type by not int"}, status=400)
    answer = a * b
    return JsonResponse({'answer': answer})


def divide_view(request):
    body = json.loads(request.body)
    a = body.get('A')
    b = body.get('B')
    try:
        a = int(a)
        b = int(b)
        answer = a / b
    except ValueError:
        return JsonResponse({'error': "Type by not int"}, status=400)
    except ZeroDivisionError:
        return JsonResponse({'error': "Division by zero"}, status=400)
    return JsonResponse({'answer': answer})
