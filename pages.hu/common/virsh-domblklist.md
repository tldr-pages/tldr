# virsh-domblklist

> A virtuális géphez tartozó blokkeszközökre vonatkozó információk listázása. Lásd még: `virsh`. További információ: <https://manned.org/virsh>.

- A blokkeszközök célnevének és forrásútvonalának felsorolása:

`virsh domblklist --domain {{vm_name}}`

- A lemez típusának és eszközértékének, valamint a célnévnek és a forrás elérési útvonalnak a felsorolása:

`virsh domblklist --domain {{vm_name}} --details`
