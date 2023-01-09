from django.shortcuts import redirect, render
from django.utils import timezone
from django.urls import reverse
from django.conf import settings


common_timezones = {
    'New York': 'America/New_York',
    'London': 'Europe/London',
    'Chennai':'Asia/Kolkata',
   
}

def visit(request):
    return render(request, 'clock/index.html', {"time":timezone.now(),"city":settings.CITY})

def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        settings.TIME_ZONE = request.POST['timezone']
        settings.CITY=get_city( request.POST['timezone'])
        
        return redirect(reverse('time'))
    else:
        return render(request, 'clock/change_time.html', {'timezones': common_timezones})

def get_city(timezone):
    for city,zone in common_timezones.items():
        if zone==timezone:
            return city
