# virsh pool-build

> Construiți sistemul de stocare de bază pentru un rezervor de stocare a mașinilor virtuale, așa cum este definit în fișierul de configurare din `/etc/libvirt/stocare`.
> A se vedea, de asemenea: `virsh`, `virsh-piscina-define-ca`, `virsh-pool-start`.
> Mai multe informaţii: <https://manned.org/virsh>

- Construiți bazinul de stocare specificat după nume sau UUID (determinați folosind lista de pool-virsh):

`virsh pool-build --pool {{name|uuid}}`
