#-*- encoding: utf-8 -*-
from django.shortcuts import render
from datetime import datetime
from timeline.models import News
from itertools import groupby


class Series(object):
	def __init__(self, date, content):
		self.date = date
		self.content = content

# Create your views here.
def all(request, top = None):
    #post_list = Article.objects.all()

    news = News.objects.order_by('-dateTime')[:top] if top is not None else News.objects.order_by('-dateTime')
    monthlyCluster = []
    for k,v in groupby(news, key = lambda x:"%d.%d" % (x.dateTime.year, x.dateTime.month)):
    	monthlyCluster.append(Series(k, list(v)))

    """
    for p in post_list:
    	p.uniqueid = '"' + p.cache + "EX"  + '"'
    	p.cache = '"' + p.cache  + '"'
    """
    return render(request, 'home.html', {'monthlyCluster' : monthlyCluster})

def home(request):
	return all(request, 90)

def test(request) :
    return render(request, 'test.html', {'current_time': datetime.now()})