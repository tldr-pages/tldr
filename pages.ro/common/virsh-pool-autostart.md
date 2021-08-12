# virsh pool-autostart

> Activați sau dezactivați autostart pentru un bazin de stocare mașină virtuală.
> A se vedea, de asemenea: `virsh`.
> Mai multe informaţii: <https://manned.org/virsh>

- Activați autostart pentru rezervorul de stocare specificat după nume sau UUID (determinați folosind `virsh pool-list`):

`virsh pool-autostart --pool {{name|uuid}}`

- Dezactivați autostart pentru rezervorul de stocare specificat după nume sau UUID:

`virsh pool-autostart --pool {{name|uuid}} --disable`
