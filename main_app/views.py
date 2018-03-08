#TODO
# Right now I'm just grabbing index 0 on the Site.objects.filter... it should be fine but I can see there could be a vulnerability there if for some dumb reason muliple objects are returned.
#
##ASSUMPTIONS
# 1. Assume that the Site model has a List of active tests.
#
#
#
from main_app.models import Site, Test_details, Variation
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import random, json

# Create your views here.

def home(request):
	return render(request, 'pages/home.html')

# TODO
# In order to keep test integrity, we'll need to pass in a user ID/ test identifier with the request
# so that we can keep a user in a specific test. 
def acubox_view(request,site_id):
	# NOTE FOR LATER: using this I can read the cookies associated with the request.
	test_container={} #initialize dictionary for all tests to be put into.
	account = Site.objects.filter(account_id=501387)[0]# account = Site.objects.filter(account_id=501387)[0] This will return the account associauted with the embed code.
	testid_list = json.loads(account.active_tests) # this will return a list of the active tests on this account.
	#TODO FOR ACTIVE TESTS CHECK PAGE TARGET PARAMETERS - should probably be some type of test setting.
	full_test_list=Test_details.objects.filter(testid__in=testid_list)
	
	for test in full_test_list:		#loop through the query set, and grab the variations for each associated test, save them in a dictionary.
		i=0
		current_test=full_test_list[i] #this gets each item of the query set in order to get the varids from each, and use them in another query
		current_variation_set=json.loads(current_test.linked_varids) #parse the current_test '[i]' as JSON 
		all_variations = Variation.objects.filter(varid__in=current_variation_set) # look for variations that have a varid in the above JSON. 
		print(all_variations)

# TODO
# This will get me a list of all the variations that I might need to serve.
# I was planning on returning these to a dictionary at the top "test_container"
# I'm realizing that in order for that list/ dictionary (whichever I decide to use) to be useful, 
# I need to have already sorted through some type of targeting checks. 
# Perhaps I should sort that out, then I'll only return the tests that pass that level of clearance. 
# That way I could use a list, then just loop through it and attempt to show all the variations that they qualify for


	all_variations = Variation.objects.filter(varid__in=dictionary['varids'])



	selection = random.randrange(2)+1
	if selection == 1:
		return render(request,'acubox/acubox-a.js')
	elif selection == 2:
		return render(request,'acubox/acubox-b.js')



# This is the solution. a list of dictionaries. 
[
	{
	'name':'varid1',
	'code':'<code>1</code>', 
	'code_type':'js', 
	'targeting_params': {
			'focus_type':'url', # could also be, cookie... or something else?
			'focus_value':'http://www.imtiredashell.com/ineedagotosleep?fuuuuuuuuuuugg=me' # Could also be cookie value... or value of w/e else I'm looking at. 
		}
	},
	{
	'name':'varid2',
	'code':'<code>2</code>', 
	'code_type':'html', 
	'targeting_params': {
			'focus_type':'cookie', # could also be, cookie... or something else?
			'focus_value':'yourmom=fat; .imtiredashell.com; expires: 11-11-2018 11:59:59' # Could also be cookie value... or value of w/e else I'm looking at. 
		}	
	}

]
