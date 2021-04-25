# virt-clone

> Clone a libvirt virtual machine.
> More information: <https://manned.org/virt-clone>.

- Clone a virtual machine and automatically generate a new name, storage path, and MAC address:

`virt-clone --original {{vm_name}} --auto-clone`

- Clone a virtual machine and specify the new name, storage path, and MAC address:

`virt-clone --original {{vm_name}} --name {{new_vm_name}} --file {{path/to/new_storage}} --mac {{ff:ff:ff:ff:ff:ff|RANDOM}}`
