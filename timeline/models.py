from django.db import models

# Create your models here.
class News(models.Model):
	cache = models.CharField(max_length = 16,primary_key = True)
	title = models.CharField(max_length = 100)
	link = models.CharField(max_length = 100)
	dateTime = models.DateTimeField()
	snippet = models.TextField()

	def __unicode__(self) :
		return self.title

	class Meta:
		ordering = ['-dateTime']
		get_latest_by = 'dateTime'