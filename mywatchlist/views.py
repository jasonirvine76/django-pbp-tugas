from django.shortcuts import render

from django.http import HttpResponse
from django.core import serializers

from mywatchlist.models import MyWatchList


# Create your views here.

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type = 'application/json')

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type = 'application/xml')

def show_html(request):
    data = MyWatchList.objects.all()
    jumlah_sudah_ditonton = 0
    for item in data:
        if item.watched:
            jumlah_sudah_ditonton += 1
    context = {
        'data':data,
        'jumlah_sudah_ditonton':jumlah_sudah_ditonton,
        'jumlah_belum_ditonton':len(data)-jumlah_sudah_ditonton
    }
    return render(request, 'mywatchlist.html', context)