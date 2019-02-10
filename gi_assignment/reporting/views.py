from django.http import JsonResponse, HttpResponseBadRequest
import requests
from datetime import datetime
import math


def total_numbers(request, start_date, end_date):
    auth_token = request.META.get('HTTP_X_GI_TOKEN')
    if not auth_token:
        return HttpResponseBadRequest('Missing header "X-Gi-Token: b64-auth-token"')
    r = requests.get('https://api.giosg.com/api/reporting/v1/rooms/'
                     '84e0fefa-5675-11e7-a349-00163efdd8db/chat-stats/daily/'
                     '?start_date={}'
                     '&end_date={}'.format(start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")),
                     headers={
                         'Authorization': 'Token '+auth_token
                     })
    stats = r.json()
    return JsonResponse({
        'total_conversation_count': stats['total_conversation_count'],
        'total_user_message_count': stats['total_user_message_count'],
        'total_visitor_message_count': stats['total_visitor_message_count']
    })


def daily_numbers(request, start_date, end_date, page=1):
    auth_token = request.META.get('HTTP_X_GI_TOKEN')
    if not auth_token:
        return HttpResponseBadRequest('Missing header "X-Gi-Token: b64-auth-token"')
    r = requests.get('https://api.gi'
                     'osg.com/api/reporting/v1/rooms/'
                     '84e0fefa-5675-11e7-a349-00163efdd8db/chat-stats/daily/'
                     '?start_date={}'
                     '&end_date={}'.format(start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")),
                     headers={
                         'Authorization': 'Token '+auth_token
                     })
    stats = r.json()
    stats_by_date = sorted(stats['by_date'], key=lambda x: datetime.strptime(x['date'], "%Y-%m-%d"))
    is_paginated = len(stats_by_date) > 5
    return JsonResponse({
        'by_date': list(map(
            lambda daily_stats: dict(
                conversation_count=daily_stats['conversation_count'],
                missed_chat_count=daily_stats['missed_chat_count'],
                visitors_with_conversation_count=daily_stats['visitors_with_conversation_count'],
                date=daily_stats['date']
            ),
            stats_by_date[(page-1)*5:(page-1)*5+5] if is_paginated else stats_by_date
        )),
        'paginated': is_paginated,
        'current_page': page,
        'max_page': math.ceil(len(stats_by_date)/5)
    })
