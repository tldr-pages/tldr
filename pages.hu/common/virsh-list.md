# virsh-list

> A virtuális gépek azonosítójának, nevének és állapotának listázása. Lásd még: `virsh`. További információ: <https://manned.org/virsh>.

- A futó virtuális gépekről szóló információk listázása:

`virsh list`

- A virtuális gépek állapotától függetlenül listázza a virtuális gépek adatait:

`virsh list --all`

- Az automatikus indítással engedélyezett vagy letiltott virtuális gépek információinak listázása:

`virsh list --all --{{autostart|no-autostart}}`

- A pillanatfelvételekkel vagy anélkül működő virtuális gépek információinak listázása:

`virsh list --all --{{with-snapshot|without-snapshot}}`
