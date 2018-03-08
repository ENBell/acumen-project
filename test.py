from main_app.models import Site, Test_details, Variation
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import random, json

dictionary={}

variations_to_load={}
account = Site.objects.filter(account_id=501387)[0]# account = Site.objects.filter(account_id=501387)[0] This will return the account associauted with the embed code.
testid_list = json.loads(account.active_tests) # this will return a list of the active tests on this account.
#TODO FOR ACTIVE TESTS CHECK PAGE TARGET PARAMETERS - should probably be some type of test setting.
full_test_list=Test_details.objects.filter(testid__in=testid_list) #gives me query set of tests associated with the Site
print(full_test_list)
for test in full_test_list:		#loop through the query set, and grab the variations for each associated test, save them in a dictionary.
	i=0
	current_test=full_test_list[i]
	current_variation_set=json.loads(current_test.linked_varids)
	all_variations = Variation.objects.filter(varid__in=current_variation_set)
	print(all_variations)


	
	i+=1
	# at the end of this I have a dictionary with the name and varids for all tests on this account.
	# now I need to load eligible varids into the randomizer to decide which gets shown.
