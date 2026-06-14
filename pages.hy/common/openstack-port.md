# openstack պորտ

> Կառավարեք OpenStack ցանցային նավահանգիստները (վիրտուալ ցանցային միջերեսներ):.
> Լրացուցիչ տեղեկություններ. <https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/port.html>:.

- Նշեք բոլոր նավահանգիստները.:

`openstack port list`

- Ցույց տալ մանրամասն տեղեկություններ կոնկրետ նավահանգստի մասին.:

`openstack port show {{port_id_or_name}}`

- Ստեղծեք նավահանգիստ որոշակի ցանցում.:

`openstack port create --network {{network_id_or_name}} {{port_name}}`

- Ստեղծեք նավահանգիստ և նշանակեք դրան ֆիքսված IP `192.168.1.50`:

`openstack port create --network {{network_id}} --fixed-ip subnet={{subnet_id}},ip-address=192.168.1.50 {{port_name}}`

- Ջնջել նավահանգիստը.:

`openstack port delete {{port_id_or_name}}`
