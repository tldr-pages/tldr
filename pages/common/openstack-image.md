# openstack image

> OpenStack Image service, aka OpenStack Glance, allows users to upload and discover data assets meant to be used with other services.
> More information: <https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/image-v2.html>.

- List available images:

`openstack image list [--public | --private | --community | --shared | --all] [--long]`

- Display image details:

`openstack image show --human-readable {{image_id}}`

- Create/upload an image:

`openstack image create [--file <file> | --volume <volume>] [--public | --private | --community | --shared] {{image_name}}`

- Delete image(s):

`openstack image delete {{image_id}} [{{image_id}} ...]`

- Save an image locally:

`openstack image save --file {{filename}} {{image_id}}`
