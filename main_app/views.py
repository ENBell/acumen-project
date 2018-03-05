from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import random

# Create your views here.

def home(request):
	return render(request, 'pages/home.html')

# First try at using a randomizer to determine which experience to serve. 
# In order to keep test integrity, we'll need to pass in a user ID/ test identifier with the request
# so that we can keep a user in a specific test. 
def acubox_view(request):
	#using this I can read the cookies associated with the request.
	print(request.COOKIES);
	selection = random.randrange(2)+1
	if selection == 1:
		return render(request,'acubox/acubox-a.js')
	elif selection == 2:
		return render(request,'acubox/acubox-b.js')