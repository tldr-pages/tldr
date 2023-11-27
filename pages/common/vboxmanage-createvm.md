# vboxmanage-createvm

> Create a new virtual machine.
> More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-createvm>.

- Create a new VM with default settings:

`VBoxManage createvm --name {{new_vm_name}}`

- Set the base folder where the VM configuration will be stored:

`VBoxManage createvm --name {{new_vm_name}} --basefolder {{path/to/directory}}`

- Set the guest OS type for the imported VM:

`VBoxManage createvm --name {{new_vm_name}} --ostype {{Ostype-from-VBoxManage-List}}`

- Register the created VM in VirtualBox:

`VBoxManage createvm --name {{new_vm_name}} --register`

- Set the VM to the specified groups:

`VBoxManage createvm --name {{new-vm_name}} --group {{group1,group2,...}}`

- Set the Universally Unique Identifier (UUID) of the VM:

`VBoxManage createvm --name {{new_vm_name}} --uuid {{UUID}}`

- Set the cipher to use for encryption:

`VBoxManage createvm --name {{new_vm_name}} --cipher {{AES-128|AES-256}}`
