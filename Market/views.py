from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'test.html')


def test(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        return render(request, 'test.html')