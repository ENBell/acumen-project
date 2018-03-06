from django.db import models

# Create your models here. These will be created in the sql database.
# for each of these I can set an option of primary_key=True in order to make that field the unique identifier. 

class Acubox(models.Model):
	name = models.CharField(max_length=250)
	contents= models.TextField()
	content_type= models.CharField(max_length=250)

	def __str__(self):
		return self.name

class Variation(models.Model):
	name = models.CharField(max_length=250) # name of the variation
	contents= models.TextField() # code/contents in the variation
	content_type_choices =(		
		('html', "HTML"),
		('js',"Javascript"),
		('css',"CSS"),
	) # this is supposed to be a picklist for the next attribute, content type
	content_type= models.CharField(max_length=250, choices=content_type_choices, default='html') # type of content this variation contains. 
	varid = models.IntegerField(default=1000) # unique id for the variation

	def __str__(self):
		return self.name

class Test_details(models.Model):
	name = models.CharField(max_length=250) # name of the test
	linked_varids =  models.CharField(max_length=10000) # ID's (varids) of the variations associated with the test
	num_variations = models.IntegerField(default=1) # of variations this test has (REMOVE? CAN'T I JUST LEN() THE LINKED VARIDS?)
	testid = models.IntegerField(default=1000) #unique id of the test

	def __str__(self):
		return self.name

class Site(models.Model):
	account_name = models.CharField(max_length=250) # account/site name
	account_id = models.CharField(max_length=250) # unique identifier for the account
	active_tests = models.TextField() # list of currently active testids
	associated_tests = models.TextField() # ID's (testids) of tests associated wit this Site/ Account 

	def __str__(self):
		return self.account_name

