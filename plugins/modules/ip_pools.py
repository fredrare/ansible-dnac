#!/usr/bin/env python3

# (c) 2019, Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible.module_utils.six import iteritems

from ansible_collections.ciscodevnet.ansible_dnac.plugins.module_utils import objects

CONFIG_TO_API_MAP = objects.KeyMap(
    ('name', 'description'),
    ('username',),
    ('password',),
    ('port',),
    ('secure',),
    ('comments',),
    ('credential_type', 'credentialType', lambda x: 'GLOBAL')
)
{
 "settings": {
    "ippool": [
      {
        "ipPoolName": "string",
        "type": "Generic",
        "ipPoolCidr": "string",
        "gateway": "string",
        "dhcpServerIps": [
          "string"
        ],
        "dnsServerIps": [
          "string"
        ],
        "IpAddressSpace": "IPv6 or IPv4"
      }
    ]
  }
}

def main():
    config_spec = {
        'name': dict(required=True),

        'username': dict(required=True),
        'password': dict(no_log=True, required=True),

        'port': dict(type='int', required=True),
        'secure': dict(type='bool'),

        'readwrite': dict(type='bool', default=False),
        'comments': dict()
    }

    argument_spec = {
        'config': dict(type='list', elements='dict', options=config_spec),
        'state': dict(choices=['present', 'absent'], default='present')
    }


    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True)

    connection = Connection(module._socket_path)

    state = module.params['state']

    result = {'changed': False}

    url = '/dna/intent/api/v1/global-pool'

    

    pass
