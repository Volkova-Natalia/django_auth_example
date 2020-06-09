from django.shortcuts import render


# Create your views here.
def home(request):
    print("home")
    print(request.method)
    return render(request, 'auth_django_inline/home.html')
