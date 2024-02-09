from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
from django.db import transaction


def mainView(request):
    return render(request, 'main/mainPage.html')


def mainTable(request):
    products = Product.objects.all().values()
    context = {'products': products}
    return render(request, 'table/table.html', context)


def savePositions(request):
    # print("Zapisano pozycje")
    if request.method == 'POST':
        try:
            # print("POST = ", request.POST)
            data = json.loads(request.body.decode('utf-8'))
            products = data.get('products', [])
            with transaction.atomic():
                for product in products:
                    index = product.get('index')
                    position = product.get('position')
                    # print(f'Index: {index}, Position: {position}')
                    product = Product.objects.get(id=index)
                    product.position = position
                    product.save()
            return JsonResponse({'success': True})
        except json.JSONDecodeError as e:
            return JsonResponse({'success': False, 'error': f'Error decoding JSON: {e}'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': f'Error processing data: {e}'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
