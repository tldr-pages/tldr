# openstack ցանց

> Կառավարեք OpenStack ցանցի ռեսուրսները:.
> Լրացուցիչ տեղեկություններ. <https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/network.html>:.

- Նշեք բոլոր ցանցերը.:

`openstack network list`

- Ցույց տալ ցանցի մանրամասները.:

`openstack network show {{network_id_or_name}}`

- Ստեղծեք նոր ցանց տվյալ անունով.:

`openstack network create {{network_name}}`

- Ջնջել ցանցը.:

`openstack network delete {{network_id_or_name}}`

- Միացնել ցանցը.:

`openstack network set --enable {{network_id_or_name}}`

- Անջատել ցանցը.:

`openstack network set --disable {{network_id_or_name}}`
