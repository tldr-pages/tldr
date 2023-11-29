# vboxmanage-clonevm

> Creates a clone of an existing virtual machine (VM).
> More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-clonevm>.

- Clone the specified VM:

`VBoxManage clonevm {{vm_name}}`

- Specify a new name for the new VM:

`VBoxManage clonevm {{vm_name}} --name {{new_vm_name}}`

- Indicate the folder where the new VM configuration is saved:

`VBoxManage clonevm {{vm_name}} --basefolder {{path/to/directory}}`

- Store the cloned VM in VirtualBox:

`VBoxManage clonevm {{vm_name}} --register`
