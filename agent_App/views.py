from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django_user_agents.utils import get_user_agent
from django.shortcuts import render

def index(request):
    return render(request, 'welcome.html')

def user_agent_info(request):
    user_agent = request.META['HTTP_USER_AGENT']
    return render(request, 'user_agent_info.html', {'user_agent': user_agent})

def device_info(request):
    user_agent = request.META['HTTP_USER_AGENT']
    is_mobile = 'Mobi' in user_agent
    is_tablet = 'Tablet' in user_agent
    is_pc = not (is_mobile or is_tablet)
    is_bot = 'Bot' in user_agent
    is_touch = request.META.get('HTTP_TOUCH', False)

    client_host = request.get_host()
    client_ip = request.META['REMOTE_ADDR']

    return render(request, 'device_info.html', {
        'is_mobile': is_mobile,
        'is_tablet': is_tablet,
        'is_pc': is_pc,
        'is_bot': is_bot,
        'is_touch': is_touch,
        'client_host': client_host,
        'client_ip': client_ip,
    })