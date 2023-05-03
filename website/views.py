from django.shortcuts import render , HttpResponse

# Create your views here.
def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')

def index(request):
    return render(request, 'website/index.html')

def resume(request):
    return render(request,'website/resume.html')