#### DOODLE Space 

from main_app.models import Variation, Test_details, Site



va = Variation(name="ian v1",contents="console.log('this is ian variation 1')",content_type="js",varid=1001)
vb = Variation(name="ian v2",contents="console.log('this is ian variation 2')",content_type="js",varid=1002)

ta = Test_details(name='MY FIRST TEST', test_id=1000, linked_varids=[1001,1002])
ta = Test_details(name='MY SECOND TEST', testid=1001, linked_varids=[])
ta = Test_details(name='MY THIRD TEST', testid=1002, linked_varids=[])

sa = Site(account_name="admin account", account_id = 501387, active_tests=[1000], associated_tests=[1000])

{
'Test_name':'NAME',
'varids':[1001,1002]
}

{
	'TESTNAME':{
			'VARID':CODE
	}
}	


exec(open("test.py").read())


for car in Car.objects.filter(id__in=(1,2)):
    print(car.license + car.vin)


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
