#!/usr/bin/python

def main():
	
	module = AnsibleModule(
   		argument_spec=dict(
        		storage=dict(default=None, required=True),
			user=dict(default='admin', required=False),
			password=dict(default='P@ssw0rd', required=False),
			vserver_name=dict(default=None, required=True),
			volume_name=dict(default=None, required=True),
			security_style=dict(default='unix', required=False),
			guarantee=dict(default='volume', required=False),
			aggr_name=dict(default=None, required=True),
		),
	)
	
	storage        = module.params['storage']
	user           = module.params['user']
	password       = module.params['password']
	vserver_name   = module.params['vserver_name']
	volume_name    = module.params['volume_name']
	security_style = module.params['security_style']
	guarantee      = module.params['guarantee']
	aggr_name      = module.params['aggr_name']

	s = NaServer(storage, 1, 20)
	s.set_admin_user(user, password)
	s.set_vserver(vserver_name)

	api = NaElement('volume-create')
	api.child_add_string('volume', volume_name)
	api.child_add_string('space-reserve', guarantee)
	api.child_add_string('containing-aggr-name', aggr_name)

	output = s.invoke_elem(api)
	#print(output.results_status())
	#print(output.sprintf())

	module.exit_json(changed=True)

from ansible.module_utils.basic import *
import sys
sys.path.append("./nmsdk")
from NaServer import *

main()
