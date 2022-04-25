from django.shortcuts import render
from django.http import *
from random import *
from string import *

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepass = ''
    len_pass = int(request.GET.get('length'))
    amount_pass = int(request.GET.get('amount'))
    upp = ascii_uppercase
    low = ascii_lowercase
    numbers = '0123456789'
    chars = low
    if request.GET.get('uppercase'):
        chars += upp
    if request.GET.get('numbers'):
        chars += numbers
    for j in range(amount_pass):
        for i in range(len_pass):
            thepass += choice(chars)
        thepass += ' '
    return render(request, 'generator/password.html', {'password': thepass})


