# virsh-undefine

> Virtuális gép törlése. További információ: <https://manned.org/virsh>.

- Csak a virtuális gép konfigurációs fájljának törlése:

`virsh undefine --domain {{vm_name}}`

- A konfigurációs fájl és az összes kapcsolódó tároló kötet törlése:

`virsh undefine --domain {{vm_name}} --remove-all-storage`

- A konfigurációs fájl és a megadott tároló kötetek törlése a cél- vagy a forrásnévvel (ahogyan azt a `virsh domblklist` parancsból megkapja):

`virsh undefine --domain {{vm_name}} --storage {{sda,path/to/source}}`
