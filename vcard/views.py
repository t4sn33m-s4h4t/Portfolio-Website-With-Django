from django.shortcuts import render, redirect
from vcard.models import *
from django.contrib import messages
# Create your views here.
def home(request):
    home = Home.objects.all()[0]
    context = {'home': home}
    return render(request, 'vcard/index.html', context)

def about(request):
    about = About.objects.all()[0]
    skills = Skill.objects.all()
    education = Education.objects.all()
    context = {'about': about, 'skills': skills, 'education': education}
    return render(request, 'vcard/about.html', context)

def portfolio(request):
    portfolios = Portfolio.objects.all()
    context = {'portfolios': portfolios}
    return render(request, 'vcard/portfolio.html', context)

def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'vcard/blog.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact_Details(name=name, email=email, subject=subject, message=message)
        contact.save()

        messages.success(request, 'Your message has been sent!')
        return redirect('/contact')
    contact = Contact.objects.all()[0]
    socials = Social.objects.all()
    context = {'contact': contact, 'socials': socials}
    return render(request, 'vcard/contact.html', context)


def post(request, slug):
    post = Blog.objects.get(id=slug)
    context = {'post': post}
    return render(request, 'vcard/post.html', context)
def handle404(request, exception):
    return render(request, '404.html')