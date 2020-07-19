import requests
from django.shortcuts import render


# Create your views here.
def index(request):
    result = None
    data = True
    global_summary = None
    while(data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            global_summary = result.json()['Global']
            data = False
        except:
            data = True
    context = {'result': result, 'global_summary': global_summary}
    return render(request, 'index.html', context)
