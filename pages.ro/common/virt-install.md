# virt-install

> Creați mașini virtuale cu libvirt și începeți instalarea sistemului de operare.
> Mai multe informaţii: <https://virt-manager.org/>

- Creați o mașină virtuală cu 1 GiB RAM și 12 giB de stocare și începeți instalarea Debian:

`virt-install --name {{vm_name}} --memory {{1024}} --disk path={{path/to/image.qcow2}},size={{12}} --cdrom {{path/to/debian.iso}}`
