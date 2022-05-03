from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Sum
from django.template import RequestContext

# Create your views here.
from hourthapp.models import HourthApp


def main(request):
    select_data = HourthApp.objects.all()
    dict_sum = {}

    for item_data in select_data:
        dict_sum.update({item_data.insertion_date: {'products': []}})

    for item_product in select_data:
        dict_sum[item_product.insertion_date]['products'].append(item_product.product)

    for data, products in dict_sum.items():
        sum_tables = {
            'competence': data,
            'sum': len(products['products'])
        }

        return render(request, 'index.html', {'select_data': select_data, 'sum': sum_tables})
