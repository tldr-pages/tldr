# VBoxManage-export

> Export virtual machines to a virtual appliance (iso) or a cloud service.
> More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-export>.

- Clone the specified VM

`VBoxManage clonevm {{The-VM}}`

- Specifies a new name for the new VM 

`VBoxManage clonevm {{The-VM}} --name {{exemple-name}}`

- Indicates the folder where the configuration of the new VM is gonna be stored.

`VBoxManage clonevm {{The-VM}} --basefolder {{path/to/directory}}`

- Store the cloned VM in VirtualBox.

`VBoxManage clonevm {{The-VM}} --register`
