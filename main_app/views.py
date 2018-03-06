#TODO
# Right now I'm just grabbing index 0 on the Site.objects.filter... it should be fine but I can see there could be a vulnerability there if for some dumb reason muliple objects are returned.
#
from main_app.models import Site, Test_details, Variation
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import random, json

# Create your views here.

def home(request):
	return render(request, 'pages/home.html')

# TFirst try at using a randomizer to determine which experience to serve. 
# In order to keep test integrity, we'll need to pass in a user ID/ test identifier with the request
# so that we can keep a user in a specific test. 
def acubox_view(request,site_id):
	# NOTE FOR LATER: using this I can read the cookies associated with the request.
	
	account = Site.objects.filter(account_id=<site_id>)[0] # This will return the account associauted with the embed code.
	tests = json.loads(account.active_tests) # this will return a list of the active tests on this account.
	#TODO FOR ACTIVE TESTS CHECK PAGE TARGET PARAMETERS - should probably be some type of test setting.
	for test in tests:
		x= Test_details.objects.filter(testid=test)
		#BOOOM THIS WILL RETURN A QUERY SET OF TESTS
		

	selection = random.randrange(2)+1
	if selection == 1:
		return render(request,'acubox/acubox-a.js')
	elif selection == 2:
		return render(request,'acubox/acubox-b.js')
