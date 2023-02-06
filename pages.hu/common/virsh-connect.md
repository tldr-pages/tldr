# virsh-connect

> Csatlakozás egy virtuális gép hipervisorához. Lásd még: `virsh`. További információ: <https://manned.org/virsh>.

- Csatlakozás az alapértelmezett hypervisorhoz:

`virsh connect`

- Csatlakozás root felhasználóként a helyi QEMU/KVM hipervizorhoz:

`virsh connect qemu:///system`

- Indítson el egy új példányt a hypervisorból, és helyi felhasználóként csatlakozzon hozzá:

`virsh connect qemu:///session`

- Csatlakozás root felhasználóként egy távoli hypervisorhoz ssh használatával:

`virsh connect qemu+ssh://{{user_name@host_name}}/system`
