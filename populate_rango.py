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
		 "url":"http://docs.python.org/2/tutorial/", "views": 20},
		{"title":"How to Think like a Computer Scientist",
		 "url":"http://www.greenteapress.com/thinkpython/", "views": 30},
		{"title":"Learn Python in 10 Minutes",
		 "url":"http://www.korokithankis.net/tutorials/python/", "views": 35} ]

	django_pages = [
	 	{"title":"Official Django Tutorial",
	 	 "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/", "views": 50},
	 	{"title":"Django Rocks",
	 	 "url":"htp://www.djangorocks.com/", "views": 25},
	 	{"title":"How to Tango with Django",
	 	 "url":"http://www.tangowithdjango.com/", "views": 5} ]

	other_pages = [
	  	{"title":"Bottle",
	  	 "url":"http;//bottlepy.org/docs/dev/", "views": 32},
	  	{"title":"Flask",
	  	 "url":"http://flask.pocoo.org", "views": 16} ]

	cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64},
	  		  "Django": {"pages": django_pages, "views": 64, "likes": 32},
	  		  "Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16}, }

# add them to the dictionaries above.


# go through cats dictionary, add each category  and then add associated pages for that directory
	for cat, cat_data in cats.iteritems():
		#c = add_cat(cat)
		c = add_cat(cat, cat_data["views"], cat_data["likes"])
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

def add_cat(name, views=0, likes=0):
	c = Category.objects.get_or_create(name=name)[0]
	c.views=views
	c.likes=likes
	c.save()
	return c


# Start execution here
if __name__ == '__main__':
	print("Starting Rango population script...")
	populate()
