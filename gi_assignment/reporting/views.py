from django.http import JsonResponse
import requests


def total_numbers(request, start_date, end_date):
    return JsonResponse({'start_date': start_date, 'end_date': end_date})


def daily_numbers(request, start_date, end_date, page=1):
    return JsonResponse({'start_date': start_date, 'end_date': end_date, 'page': page})

