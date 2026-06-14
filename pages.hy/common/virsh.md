# virsh

> Կառավարեք `virsh` հյուրի տիրույթները:.
> Նշում. Ստորև բերված հրամաններից մի քանիսը կարող են պահանջել հստակ նշել `virsh --connect URI`:.
> Որոշ ենթահրամաններ, ինչպիսիք են `list`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://libvirt.org/manpages/virsh.html>:.

- Ինտերակտիվ կերպով միացեք հիպերվիզորի նիստին.:

`virsh {{[-c|--connect]}} {{qemu:///system|qemu:///session|xen:///system|lxc:///system|...}}`

- Նշեք բոլոր տիրույթները.:

`virsh {{[-c|--connect]}} {{uri}} list --all`

- Ակտիվացրեք `default` անունով ցանցը՝:

`sudo virsh net-start {{default}}`

- Ստեղծեք տիրույթ կազմաձևման ֆայլից.:

`sudo virsh create {{path/to/config_file.xml}}`

- Խմբագրել տիրույթի կազմաձևման ֆայլը (խմբագիրը կարող է փոխվել `$EDITOR` կամ `$VISUAL`-ով):

`sudo virsh edit {{domain}}`

- Սկսել/վերագործարկել/վերակայել/անջատել/ոչնչացնել/կասեցնել/վերսկսել տիրույթը.:

`sudo virsh {{start|reboot|reset|shutdown|destroy|suspend|resume}} {{domain}}`

- Պահպանեք տիրույթի ընթացիկ գործարկման վիճակը (RAM, բայց ոչ սկավառակի վիճակը) պետական ֆայլում (տիրույթն անջատված կլինի).:

`sudo virsh save {{domain}} {{path/to/state_file}}`

- Հեռացրեք դադարեցված տիրույթի պահեստը և լուսանկարները.:

`sudo virsh undefine {{domain}} --remove-all-storage --snapshots-metadata`
