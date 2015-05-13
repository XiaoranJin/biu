#-*- encoding: utf-8 -*-

# start django 
import os,django,re
os.environ['DJANGO_SETTINGS_MODULE'] = 'biu.settings'
from django.conf import settings
django.setup()


# do Updating
from datetime import datetime
import json,urllib2,sys
from timeline.models import News

def insertJson(searchResult):
	for item in searchResult["items"]:
		cache = item['cacheId']
		title = item['title']
		link = item['link']
		snippet = item['snippet']
		datestring = re.search('/t([0-9]{8})_',link).group(1)
		dateTime = datetime.strptime(datestring,"%Y%m%d")

		if News.objects.filter(cache=cache).exists():
			continue
			
		#print cache,title,link,snippet,dateTime
		newsObject = News(title = title, cache = cache, link = link, snippet = snippet, dateTime= dateTime)
		try:
			newsObject.save()
			print u"Insert: %s" % title
		except Exception, e:
			print e

"""
for page in range(1,11):
	searchResult = json.load(open("../htmltest/%d.json" % page))
	insertJson(searchResult)
"""

baseurl = "https://www.googleapis.com/customsearch/v1?cx=011796648310020391649%3Antkstgdw2uo&q=%E9%BB%84%E5%90%AF%E5%93%B2&dateRestrict=d2"

key = sys.argv[1]
url = baseurl + "&key=%s" % key

try:
	respond = urllib2.urlopen(url).read()
	searchResult = json.loads(respond)
except urllib2.URLError, e:
	print e

insertJson(searchResult)



"""
n = News(title = 'Hello World', cache ='test', link = 'Python', snippet = u'我们来做一个简单的数据库增加操作', dateTime=date(1990,1,1))

n.save()
print News.objects.all() 
a = News.objects.filter(cache="test")
a.delete()
print News.objects.all()
"""