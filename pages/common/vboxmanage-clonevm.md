# vboxmanage-clonevm

> Creates a clone of an existing virtual machine (VM).
> More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-clonevm>.

- Clone the specified VM:

`VBoxManage clonevm {{vm_name}}`

- Specifies a new name for the new VM:

`VBoxManage clonevm {{The-VM}} --name {{exemple-name}}`

- Indicates the folder where the configuration of the new VM is gonna be stored:

`VBoxManage clonevm {{The-VM}} --basefolder {{path/to/directory}}`

- Store the cloned VM in VirtualBox:

`VBoxManage clonevm {{The-VM}} --register`
