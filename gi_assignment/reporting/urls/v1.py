from django.urls import path, register_converter
from .. import converters, views

register_converter(converters.DateConverter, 'date')  # YYYY-MM-DD
register_converter(converters.PageConverter, 'page')  # page-1, page-2, etc.

# reporting/v1/
urlpatterns = [
    path('total/from-<date:start_date>/to-<date:end_date>/', views.total_numbers),
    path('daily/from-<date:start_date>/to-<date:end_date>/', views.daily_numbers),
    path('daily/from-<date:start_date>/to-<date:end_date>/<page:page>/', views.daily_numbers)
]
