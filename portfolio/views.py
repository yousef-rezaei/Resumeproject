from django.shortcuts import render , HttpResponse

# Create your views here.

def portfolio_details(request):
    return render(request, 'portfolio/portfolio-details.html')

def portfolio(request):
    return render(request, 'portfolio/portfolio.html')