# Import category and page model
from rango.models import Category
from rango.models import Page
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	#Query db for a list of ALL stored categories. Orderby likes in descending order. Retrieve top5 only.
	#Place the list in context_dict dictionary which will be passed to the template engine.
	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {'categories': category_list}

	#Return a rendered response. It's a shortcut function. The first parameter is the tamplate we want to use.
	return render(request, 'rango/index.html', context_dict)

def about(request):
	context_dict = {'boldmessage': "This is the bold message."}
	return render(request, 'rango/about.html', context=context_dict)

#def show_category(request, category_name_slug):
#	context_dict = {}

#	try:
#		category = Category.objects.get(slug=category_name_slug)
#		pages = Page.objects.filter(category=category)
#		context_dict['pages'] = pages
#		context_dict['category'] = category
#	except Category.DoesNotExist:
#		context_dict['category'] = None
#		context_dict['pages'] = None

#	return render(request, 'rango/category.html', context_dict)

#	return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about'>About</a>")

#def about(request):
#	return HttpResponse("Rango says here is the about page. <br/> <a href='/rango/'>Index</a>")
