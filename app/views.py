from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'Rakesh','age':9}
    return render(request,'jinja_print.html',context=d) 