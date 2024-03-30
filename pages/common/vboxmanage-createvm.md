# vboxmanage-createvm

> Create a new virtual machine.
> More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-createvm>.

- Create a new VM with default settings:

`VBoxManage createvm --name {{vm_name}}`

- Set the base folder where the VM configuration will be stored:

`VBoxManage createvm --name {{vm_name}} --basefolder {{path/to/directory}}`

- Set the guest OS type (one of `VBoxManage list ostypes`) for the imported VM:

`VBoxManage createvm --name {{vm_name}} --ostype {{ostype}}`

- Register the created VM in VirtualBox:

`VBoxManage createvm --name {{vm_name}} --register`

- Set the VM to the specified groups:

`VBoxManage createvm --name {{vm_name}} --group {{group1,group2,...}}`

- Set the Universally Unique Identifier (UUID) of the VM:

`VBoxManage createvm --name {{vm_name}} --uuid {{uuid}}`

- Set the cipher to use for encryption:

`VBoxManage createvm --name {{vm_name}} --cipher {{AES-128|AES-256}}`
