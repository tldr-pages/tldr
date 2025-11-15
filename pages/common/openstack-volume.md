# openstack volume

> Manage OpenStack volumes.
> OpenStack Block Storage service, aka OpenStack Cinder, provides volumes to Nova vm's, Ironic bare-metal hosts, containers, and others.
> More information: <https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/volume.html>.

- List volumes:

`openstack volume list --all-projects`

- Show volume details:

`openstack volume show {{volume_id}}`

- Create new volume:

`openstack volume create --size {{size_in_GB}} --image {{image_id}} --snapshot {{snapshot_id}} {{--bootable|--non-bootable}} {{volume_name}}`

- Delete volumes(s):

`openstack volume delete {{volume_id1 volume_id2 ...}}`

- Migrate volume to a new host:

`openstack volume migrate --host {{host_hostname}} {{instance_id}}`

- Set volume properties:

`openstack volume set --name {{volume_new_name}} --size {{volume_new_size}} {{--attached|--detached}} {{--bootable|--non-bootable}} {{volume_id}}`
