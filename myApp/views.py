from django.shortcuts import render
from myApp.models import skill

# Create your views here.

def index(request):
    skills_list = skill.objects.all()
    return render(request, "mystar/index.html", {'skills': skills_list})
def about(request):
    return render(request, "mystar/about.html")
def contact(request):
    return render(request, "mystar/contact.html")
def pricing(request):
    return render(request, "mystar/pricing.html")
def faqs(request):
    return render(request, "mystar/faq.html")
def blogs_home(request):
    return render(request, "mystar/blog-home.html")
def blogs_posts(request):
    return render(request, "mystar/blog-post.html")
def portfolio_overview(request):
    return render(request, "mystar/portfolio-overview.html")
def portfolio_items(request):
    return render(request, "mystar/portfolio-item.html")
