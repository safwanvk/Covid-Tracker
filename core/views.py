import requests
from django.shortcuts import render


# Create your views here.
def index(request):
    result = None
    data = True
    global_summary = None
    countries = None
    while(data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            json = result.json()
            global_summary = json['Global']
            countries = json['Countries']
            data = False
        except:
            data = True
    context = {'result': result, 'global_summary': global_summary, 'countries': countries}
    return render(request, 'index.html', context)
