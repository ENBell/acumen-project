from django.db import models

# Create your models here.

class Acubox(models.Model):
	name = models.CharField(max_length=250)
	contents= models.TextField()
	content_type= models.CharField(max_length=250)

	def __str__(self):
		return self.name

class Variation(models.Model):
	name = models.CharField(max_length=250)
	contents= models.TextField()
	content_type_choices =(		
		('html', "HTML"),
		('js',"Javascript"),
		('css',"CSS"),
	)
	content_type= models.CharField(max_length=250, choices=content_type_choices, default='html')
	varid = models.IntegerField()

	def __str__(self):
		return self.name

class Test_details(models.Model):
	name = models.CharField(max_length=250)
	linked_varids =  models.CharField(max_length=10000)
	num_variations = models.IntegerField()

	def __str__(self):
		return self.name
# 		