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
def home(request):
    #post_list = Article.objects.all()
    news = News.objects.order_by('-dateTime')[:80]
    monthlyCluster = []
    for k,v in groupby(news, key = lambda x:"%d.%d" % (x.dateTime.year, x.dateTime.month)):
    	monthlyCluster.append(Series(k, list(v)))

    """
    for p in post_list:
    	p.uniqueid = '"' + p.cache + "EX"  + '"'
    	p.cache = '"' + p.cache  + '"'
    """
    return render(request, 'home.html', {'monthlyCluster' : monthlyCluster})

def test(request) :
    return render(request, 'test.html', {'current_time': datetime.now()})