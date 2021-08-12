# virt-sysprep

> Resetați, deconfigurați sau particularizați o imagine de mașină virtuală.
> Mai multe informaţii: <https://manned.org/virt-sysprep>

- Lista tuturor operațiilor acceptate (operațiile activate sunt indicate cu asteriscuri):

`virt-sysprep --list-operations`

- Rulați toate operațiunile activate, dar nu aplicați de fapt modificările:

`virt-sysprep --domain {{vm_name}} --dry-run`

- Rulați numai operațiunile specificate:

`virt-sysprep --domain {{vm_name}} --operations {{operation1,operation2,...}}`

- Generați un nou fișier `/etc/machine id` și activați personalizările pentru a putea schimba numele gazdei pentru a evita conflictele de rețea:

`virt-sysprep --domain {{vm_name}} --enable {{customizations}} --hostname {{host_name}} --operation {{machine-id}}`
