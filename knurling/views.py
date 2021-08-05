from django.shortcuts import render

def index(request):
    return render(request, 'knurling/index.html')

def about(request):
    return render(request, 'knurling/about.html')

def members(request):
    return render(request, 'knurling/members.html')

def contact(request):
    return render(request,'knurling/contact.html')