from django.shortcuts import render,HttpResponse

# Create your views here.
def display(request):
    return HttpResponse('<h3>Please reach to us contact@example.com for any queries.</h3>')


