#### DOODLE Space 

from main_app.models import Variation, Test_details, Site



va = Variation(name="ian v1",contents="console.log('this is ian variation 1')",content_type="js",varid=1001)
vb = Variation(name="ian v2",contents="console.log('this is ian variation 2')",content_type="js",varid=1002)

ta = Test_details(name='MY FIRST TEST', test_id=1000, linked_varids=[1001,1002])
ta = Test_details(name='MY SECOND TEST', testid=1001, linked_varids=[])
ta = Test_details(name='MY THIRD TEST', testid=1002, linked_varids=[])

sa = Site(account_name="admin account", account_id = 501387, active_tests=[1000], associated_tests=[1000])