# openstack image

> OpenStack Image service, aka OpenStack Glance, allows users to upload and discover data assets meant to be used with other services.
> More information: <https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/image-v2.html>.

- List available images:

`openstack image list {{--private|--shared|--all}}`

- Display image details:

`openstack image show --human-readable {{image_id}}`

- Create/upload an image:

`openstack image create --file {{path/to/file}} {{--private|--shared|--all}} {{image_name}}`

- Delete image(s):

`openstack image delete {{image_id1 image_id2 ...}}`

- Save an image locally:

`openstack image save --file {{filename}} {{image_id}}`
