# openstack համ

> Կառավարեք OpenStack-ի օրինակների համը (վիրտուալ ապարատային կաղապարներ):.
> Լրացուցիչ տեղեկություններ. <https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/flavor.html>:.

- Թվարկեք բոլոր համերը.:

`openstack flavor list`

- Ցույց տալ համի մանրամասները.:

`openstack flavor show {{flavor_id_or_name}}`

- Ստեղծեք նոր համ 2 vCPU-ով, 4GB RAM-ով և 20GB սկավառակով.:

`openstack flavor create {{flavor_name}} --vcpus 2 --ram 4096 --disk 20`

- Ջնջել համը.:

`openstack flavor delete {{flavor_id_or_name}}`

- Ստեղծեք համը 10 ԳԲ ժամանակավոր սկավառակով և 512 ՄԲ փոխանակման տարածքով.:

`openstack flavor create {{flavor_name}} --vcpus 4 --ram 8192 --disk 40 --ephemeral 10 --swap 512`
