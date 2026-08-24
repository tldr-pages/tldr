# iscsiadm

> Manage iSCSI sessions, nodes, and discovery.
> More information: <https://manned.org/iscsiadm>.

- Show active iSCSI sessions:

`sudo iscsiadm {{[-m|--mode]}} session`

- List all known iSCSI nodes:

`sudo iscsiadm {{[-m|--mode]}} node`

- Discover available iSCSI targets on a portal (no authentication):

`sudo iscsiadm {{[-m|--mode]}} discovery {{[-t|--type]}} sendtargets {{[-p|--portal]}} {{ip_address}}`

- Log in to a specific iSCSI target without authentication:

`sudo iscsiadm {{[-m|--mode]}} node {{[-T|--targetname]}} {{iqn}} {{[-p|--portal]}} {{ip_address}}:3260 {{[-l|--login]}}`

- Log out from a specific iSCSI target:

`sudo iscsiadm {{[-m|--mode]}} node {{[-T|--targetname]}} {{iqn}} {{[-p|--portal]}} {{ip_address}}:3260 {{[-u|--logout]}}`

- Create an iSCSI node when discovery is blocked (for CHAP authentication):

`sudo iscsiadm {{[-m|--mode]}} node {{[-o|--op]}} new {{[-T|--targetname]}} {{iqn}} {{[-p|--portal]}} {{ip_address}}:3260`

- Configure CHAP authentication for an iSCSI target:

`sudo iscsiadm {{[-m|--mode]}} node {{[-T|--targetname]}} {{iqn}} {{[-p|--portal]}} {{ip_address}}:3260 {{[-o|--op]}} update {{[-n|--name]}} node.session.auth.authmethod {{[-v|--value]}} CHAP`
