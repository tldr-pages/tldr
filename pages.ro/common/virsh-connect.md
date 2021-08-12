# virsh-connect

> Conectați-vă la un hipervizor mașină virtuală.
> A se vedea, de asemenea: `virsh`.
> Mai multe informaţii: <https://manned.org/virsh>

- Conectați-vă la hipervizorul implicit:

`virsh connect`

- Conectați-vă ca rădăcină la hipervizorul local QEMU/KVM:

`virsh connect qemu:///system`

- Lansați o nouă instanță a hipervizorului și conectați-vă la acesta ca utilizator local:

`virsh connect qemu:///session`

- Conectați-vă ca root la un hipervizor de la distanță folosind ssh:

`virsh connect qemu+ssh://{{user_name@host_name}}/system`
