from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, 'passwordproj/home.html')
def about(request):
    return render(request, 'passwordproj/about.html')
def password(request):
    
    characters = list('abcdefghijklmopqrstuvwxyz')
    if request.GET.get('numeric'):
        characters.extend(list('1234567890'))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))
    length = int(request.GET.get('length', 12))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'passwordproj/password.html', {'password':thepassword})
