#!/usr/bin/python

def main():

        module = AnsibleModule(
                argument_spec=dict(
                        storage=dict(default=None, required=True),
                        user=dict(default='admin', required=False),
                        password=dict(default='P@ssw0rd', required=False),
                        vserver_name=dict(default=None, required=True),
			root_volume=dict(default='svm_root', required=False),
			root_volume_aggregate=dict(default=None, required=True),
			root_volume_security_style=dict(default='unix', required=False),
                ),
        )

        storage        = module.params['storage']
        user           = module.params['user']
        password       = module.params['password']
        vserver_name   = module.params['vserver_name']
	root_volume    = module.params['root_volume']
	root_volume_aggregate      = module.params['root_volume_aggregate']
	root_volume_security_style = module.params['root_volume_security_style']

	s = NaServer(storage, 1, 20)
	s.set_admin_user(user, password)

	api = NaElement('vserver-create')
	api.child_add_string('language','C');
	ns_switch = NaElement('name-server-switch');
	api.child_add(ns_switch)

	ns_switch.child_add_string('nsswitch','file')
	api.child_add_string('root-volume', root_volume)
	api.child_add_string('root-volume-aggregate', root_volume_aggregate)
	api.child_add_string('root-volume-security-style', root_volume_security_style)
	api.child_add_string('vserver-name', vserver_name);

	output = s.invoke_elem(api)
	module.exit_json(changed=True)

from ansible.module_utils.basic import *
import sys
sys.path.append("./nmsdk")
from NaServer import *

main()
