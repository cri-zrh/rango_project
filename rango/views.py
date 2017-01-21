from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	#Construct a dictionary to pass to the template engine as it's context. 
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
	#Return a rendered response. It's a shortcut function. The first parameter is the tamplate we want to use.
	return render(request, 'rango/index.html', context=context_dict)

def about(request):
	context_dict = {'boldmessage': "This is the bold message."}
	return render(request, 'rango/about.html', context=context_dict)
