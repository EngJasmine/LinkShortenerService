from django.shortcuts import render,get_object_or_404, redirect
from .models import Link
from .forms import LinkForm
from django.urls import reverse

# Create your views here.
def index(request):
    links = Link.objects.all()
    context = {
        "links":links
    }
    return render(request,'links/index.html',context)

def root_link(request,slug_link):
    link = get_object_or_404(Link, slug=slug_link)
    link.click() # This will increment the clicked field

    return redirect(link.url)

def add_link(request):
    if request.method == 'POST':
        # form has data
        form = LinkForm(request.POST)
        if form.is_valid():
            # save the data  and return user to homepage
            form.save()
            return redirect(reverse('home'))
            
    else:
            form = LinkForm()

    context = {
            "form": form
            }
    return render(request,'links/create.html',context)