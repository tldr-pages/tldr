# vboxmanage movevm

> Mueve una máquina virtual (VM) a una nueva ubicación en el sistema anfitrión.
> Más información: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-movevm>.

- Mueve la máquina virtual especificada a la ubicación actual:

`VBoxManage movevm {{nombre_vm}}`

- Especifica la nueva ubicación (nombre de ruta completo o relativo) de la máquina virtual:

`VBoxManage movevm {{nombre_vm}} --folder {{ruta/a/nueva_ubicación}}`
