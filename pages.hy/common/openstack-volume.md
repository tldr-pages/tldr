# openstack ծավալը

> Կառավարեք OpenStack-ի ծավալները:.
> OpenStack Block Storage ծառայությունը, որը կոչվում է OpenStack Cinder, տրամադրում է ծավալներ Nova vm's-ին, Ironic bare-metal hosts-ներին, բեռնարկղերին և այլն:.
> Լրացուցիչ տեղեկություններ. <https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/volume.html>:.

- Ցանկի ծավալները.:

`openstack volume list --all-projects`

- Ցույց տալ ծավալի մանրամասները.:

`openstack volume show {{volume_id}}`

- Ստեղծեք նոր ծավալ.:

`openstack volume create --size {{size_in_GB}} --image {{image_id}} --snapshot {{snapshot_id}} {{--bootable|--non-bootable}} {{volume_name}}`

- Ջնջել հատորները.:

`openstack volume delete {{volume_id1 volume_id2 ...}}`

- Տեղափոխել ծավալը նոր հյուրընկալող.:

`openstack volume migrate --host {{host_hostname}} {{instance_id}}`

- Սահմանեք ծավալի հատկությունները.:

`openstack volume set --name {{volume_new_name}} --size {{volume_new_size}} {{--attached|--detached}} {{--bootable|--non-bootable}} {{volume_id}}`
