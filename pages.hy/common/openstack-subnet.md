# openstack ենթացանց

> Կառավարեք OpenStack ենթացանցերը (IP հասցեների բլոկները ցանցում):.
> Լրացուցիչ տեղեկություններ. <https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/subnet.html>:.

- Նշեք բոլոր ենթացանցերը.:

`openstack subnet list`

- Ցույց տալ կոնկրետ ենթացանկի մանրամասները.:

`openstack subnet show {{subnet_id_or_name}}`

- Ցուցակե՛ք ցանցի հետ կապված ենթացանցերը.:

`openstack subnet list --network {{network_id_or_name}}`

- Ստեղծեք ենթացանց՝ `192.168.0.0/24` ենթացանցով տվյալ ցանցում.:

`openstack subnet create --network {{network_id_or_name}} --subnet-range 192.168.0.0/24 {{subnet_name}}`

- Ջնջել ենթացանցը.:

`openstack subnet delete {{subnet_id_or_name}}`

- Թարմացրեք ենթացանցը DNS `8.8.8.8`-ով և սահմանեք նոր անուն.:

`openstack subnet set --dns-nameserver 8.8.8.8 --name {{new_subnet_name}} {{subnet_id}}`
