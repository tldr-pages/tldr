# virsh pool-undefine

> Ștergeți fișierul de configurare în `/etc/libvirt/stocare` pentru un rezervor de stocare mașină virtuală oprit.
> A se vedea de asemenea: `virsh`, `virsh-piscina — distruge”.
> Mai multe informaţii: <https://manned.org/virsh>

- Ștergeți configurația pentru numele specificat al bazinului de stocare sau UUID (determinați folosind `virsh pool-list`):

`virsh pool-undefine --pool {{name|uuid}}`
