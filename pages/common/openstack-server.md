# openstack server

> Manage OpenStack virtual machines.
> OpenStack Compute service, aka OpenStack Nova, mainly hosts and manages cloud computing systems.
> More information: <https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/server.html>.

- List servers:

`openstack server list`

- Start server(s):

`openstack server start {{instance_id1 instance_id2 ...}}`

- Stop server:

`openstack server stop {{instance_id1 instance_id2 ...}}`

- Create new server:

`openstack server create --image {{image_id}} --flavor {{flavor_id}} --network {{network_id}} --wait {{server_name}}`

- Delete server(s):

`openstack server delete {{instance_id1 instance_id2 ...}}`

- Migrate server to different host:

`openstack server migrate --live {{host_hostname}} {{--shared-migration|--block-migration}} --wait {{instance_id}}`

- Perform a soft or hard reset to the server:

`openstack server reboot {{--soft|--hard}} --wait {{instance_id}}`
