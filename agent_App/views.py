from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django_user_agents.utils import get_user_agent
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def device_info(request):
    #Casudísticas que se deben dar
    is_mobile = request.user_agent.is_mobile
    is_tablet = request.user_agent.is_tablet
    is_touch = request.user_agent.is_touch_capable
    is_pc = request.user_agent.is_pc
    is_bot = request.user_agent.is_bot

    #Una forma distinta para mostrarlo después en el template
    if is_touch:
        is_touch = 'Sí'
    else:
        is_touch = 'No'

    # Buscado en https://stackoverflow.com/questions/75374097/django-v4-request-metaremote-addr-not-working-anymore
    # Nos da la IP del host y cliente

    host_ip = request.META.get('SERVER_ADDR', 'Desconocida')
    client_ip = request.META.get('REMOTE_ADDR', 'Desconocida')

    return render(request, 'device_info.html', {
        'is_mobile': is_mobile,
        'is_tablet': is_tablet,
        'is_pc': is_pc,
        'is_bot': is_bot,
        'is_touch': is_touch,
        'host_ip': host_ip,
        'client_ip': client_ip,
    })