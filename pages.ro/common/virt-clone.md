# virt-clone

> Clona o mașină virtuală libvirt.
> Mai multe informaţii: <https://manned.org/virt-clone>

- Clonează o mașină virtuală și generează automat un nume nou, calea de stocare și adresa MAC:

`virt-clone --original {{vm_name}} --auto-clone`

- Clona o mașină virtuală și specificați noul nume, calea de stocare și adresa MAC:

`virt-clone --original {{vm_name}} --name {{new_vm_name}} --file {{path/to/new_storage}} --mac {{ff:ff:ff:ff:ff:ff|RANDOM}}`
