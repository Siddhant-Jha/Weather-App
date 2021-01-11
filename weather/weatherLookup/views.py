from django.shortcuts import render

def home (request):
    import json
    import requests

    api_request = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Delhi,india&APPID=4b1b1c24cb4a6c52a38d525bd418cb12')

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."
    
    return render (request, 'index.html', {'api':api})


def about (request):
    return render (request, 'about.html', {})