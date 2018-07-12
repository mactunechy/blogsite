from django.shortcuts import render , redirect
from .models import *
from .forms import *
from django.views.generic import ListView,DetailView,CreateView, FormView


# Create your views here.
def blog(request):
	qs1 = Blog.objects.all().order_by("-pub_date")[:4]
	qs = Blog.objects.all().order_by("-pub_date")
	context = {
		'bloglist':qs,
		'bloglists':qs1
	}
	template_name = 'bloglist.html'
	return render(request,template_name,context)

def blogdetail(request,id):
	qs1 = Blog.objects.all().order_by("-pub_date")[:4]
	qs = Blog.objects.get(pk=id)
	context = {
		'blogdetail':qs,
		'bloglists':qs1
	}
	template_name = 'blogdetail.html'
	return render(request,template_name,context)
	
def contact(request):
	qs1 = Blog.objects.all().order_by("-pub_date")[:4]
	context = {
		"bloglists":qs1
	}
	template_name = 'contact.html'
	return render(request,template_name,context)
				
def about(request):
	qs1 = Blog.objects.all().order_by("-pub_date")[:5]
	context = {
	"bloglists":qs1
	}
	template_name = 'about.html'
	return render(request,template_name,context)

class Post(CreateView):
	model=Blog
	template_name ="post_new.html"
	fields = ('title','content','image')
	success_url = '/'

						

										
class ContactForm(FormView):
	form_class=ContactForm
	template_name = 'contact.html'
	success_url='/contact'
																															