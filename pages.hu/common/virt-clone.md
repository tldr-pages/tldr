# virt-clone

> Egy libvirt virtuális gép klónozása. További információ: <https://manned.org/virt-clone>.

- Egy virtuális gép klónozása és egy új név, tárolási útvonal és MAC-cím automatikus generálása:

`virt-clone --original {{vm_name}} --auto-clone`

- Virtuális gép klónozása és az új név, tárolási útvonal és MAC-cím megadása:

`virt-clone --original {{vm_name}} --name {{new_vm_name}} --file {{path/to/new_storage}} --mac {{ff:ff:ff:ff:ff:ff|RANDOM}}`
