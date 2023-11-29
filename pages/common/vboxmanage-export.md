# vboxmanage-export

> Export virtual machines to a virtual appliance (ISO) or a cloud service.
> More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-export>.

- Clone the specified VM:

`VBoxManage clonevm {{vm_name}}`

- Set a new name for the new VM:

`VBoxManage clonevm {{vm_name}} --name {{example_name}}`

- Indicate the folder where the configuration of the new VM will be stored:

`VBoxManage clonevm {{vm_name}} --basefolder {{path/to/directory}}`

- Store the cloned VM in VirtualBox:

`VBoxManage clonevm {{vm_name}} --register`
