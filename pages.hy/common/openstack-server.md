# openstack սերվեր

> Կառավարեք OpenStack վիրտուալ մեքենաները:.
> OpenStack Compute ծառայությունը, որը կոչվում է OpenStack Nova, հիմնականում հյուրընկալում և կառավարում է ամպային հաշվողական համակարգերը:.
> Լրացուցիչ տեղեկություններ. <https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/server.html>:.

- Ցուցակ սերվերներ.:

`openstack server list`

- Սկսել սերվեր(ներ).:

`openstack server start {{instance_id1 instance_id2 ...}}`

- Դադարեցրեք սերվերը.:

`openstack server stop {{instance_id1 instance_id2 ...}}`

- Ստեղծեք նոր սերվեր.:

`openstack server create --image {{image_id}} --flavor {{flavor_id}} --network {{network_id}} --wait {{server_name}}`

- Ջնջել սերվեր(ներ).:

`openstack server delete {{instance_id1 instance_id2 ...}}`

- Տեղափոխել սերվերը տարբեր հոսթին.:

`openstack server migrate --live {{host_hostname}} {{--shared-migration|--block-migration}} --wait {{instance_id}}`

- Կատարեք փափուկ կամ կոշտ վերականգնում սերվերի վրա.:

`openstack server reboot {{--soft|--hard}} --wait {{instance_id}}`
