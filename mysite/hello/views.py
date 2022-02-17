from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def sessfun(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    resp = HttpResponse('view count='+str(num_visits))
    resp.set_cookie('dj4e_cookie', '4c26b0f5', max_age=1000)
    return resp

def email(request):
    send_mail('Hey, Sending from Ivan', 'Hi Bowen, how are you doing. Yeey!! You learnt django mails', 'ivanovicbow850@gmail.com', ['bowenivan16@gmail.com'], fail_silently=False)
    return render(request, 'hello/email.html')