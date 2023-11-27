# vboxmanage-export

> Export virtual machines to a virtual appliance (iso) or a cloud service.
> More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-export>.

- Clone the specified VM:

`VBoxManage clonevm {{vm_name}}`

- Set a new name for the new VM:

`VBoxManage clonevm {{vm_name}} --name {{exemple_name}}`

- Indicate the folder where the configuration of the new VM is gonna be stored:

`VBoxManage clonevm {{vm_name}} --basefolder {{path/to/directory}}`

- Store the cloned VM in VirtualBox:

`VBoxManage clonevm {{vm_name}} --register`
