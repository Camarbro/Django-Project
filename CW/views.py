from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'CW/home.html')

def admin(request):
    return render(request, 'CW/admin.html')
