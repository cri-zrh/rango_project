import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
					  'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
	# First create a list of dictionaires containing pages.
	# Then create dictionary of dictionaries for categories. This allows to iterate through each data structre and add data tou the models.

	python_pages = [
		{"title": "Official Python Tutorial",
		 "url":"http://docs.python.org/2/tutorial/"},
		{"title":"How to Think like a Computer Scientist",
		 "url":"http://www.greenteapress.com/thinkpython/"},
		{"title":"Learn Python in 10 Minutes",
		 "url":"http://www.korokithankis.net/tutorials/python/"} ]

	django_pages = [
	 	{"title":"Official Django Tutorial",
	 	 "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
	 	{"title":"Django Rocks",
	 	 "url":"htp://www.djangorocks.com/"},
	 	{"title":"How to Tango with Django",
	 	 "url":"http://www.tangowithdjango.com/"} ]

	other_pages = [
	  	{"title":"Bottle",
	  	 "url":"http;//bottlepy.org/docs/dev/"},
	  	{"title":"Flask",
	  	 "url":"http://flask.pocoo.org"} ]

	cats = {"Python": {"pages": python_pages},
	  		  "Django": {"pages": django_pages},
	  		  "Other Frameworks": {"pages": other_pages} }

# add them to the dictionaries above.


# go through cats dictionary, add each category  and then add associated pages for that directory
	for cat, cat_data in cats.iteritems():
		c = add_cat(cat)
		for p in cat_data["pages"]:
			add_page(c, p["title"], p["url"])

# print out the added categories
	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
	p = Page.objects.get_or_create(category=cat, title=title)[0]
	p.url=url
	p.views=views
	p.save()
	return p

def add_cat(name):
	c = Category.objects.get_or_create(name=name)[0]
	c.views=0
	c.likes=0
	c.save()
	return c

# Set default views and likes for category Python
def add_cat(Python):
	python = Category.objects.get_or_create(name="Python")[0]
	python.views=64
	python.likes=32
	python.save()
	return python

# Set default views and likes for category Other Frankeworks
def add_cat(other_pages):
	of = Category.objects.get_or_create(name="Other Frameworks")[0]
	of.views=32
	of.likes=16
	of.save()
	return of

# Start execution here
if __name__ == '__main__':
	print("Starting Rango population script...")
	populate()
