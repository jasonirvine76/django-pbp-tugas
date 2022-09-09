from django.shortcuts import render

from katalog.models import CatalogItem

# TODO: Create your views here.

def katalog(request):
    catalog_item_list = CatalogItem.objects.all()
    context = {
        'nama': 'Jason Irvine Mahendra Putra',
        'npm' : '2106750654',
        'data': catalog_item_list,
    }
    return render(request, 'katalog.html', context)