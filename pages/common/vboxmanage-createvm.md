# vboxmanage-createvm

> Create a new virtual machine.
> More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-createvm>.

- Create a new VM with default settings:

`VBoxManage createvm --name {{new-vm-name}}`

- Set the base folder where the VM configuration will be stored:

`VBoxManage createvm --name {{new-vm-name}} --basefolder {{path/to/directory}}`

- Set the guest OS type for the imported VM:

`VBoxManage createvm --name {{new-vm-name}} --ostype {{Ostype-from-VBoxManage-List}}`

- Register the created VM in VirtualBox:

`VBoxManage createvm --name {{new-vm-name}} --register`

- Assigns the VM to the specified groups:

`VBoxManage createvm --name {{new-vm-name}} --group {{group1,group2,...}}`

- Specifies the Universally Unique Identifier (UUID) of the VM:

`VBoxManage createvm --name {{new-vm-name}} --uuid {{UUID}}`

- Specifies the cipher to use for encryption:

`VBoxManage createvm --name {{new-vm-name}} --cipher {{AES-128|AES-256}}`
