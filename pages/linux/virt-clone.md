# virt-clone

> Clone a libvirt virtual machine.
> More information: <https://manned.org/virt-clone>.

- Clone a virtual machine and automatically generate a new name, storage path, and MAC address:

`virt-clone {{[-o|--original]}} {{vm_name}} --auto-clone`

- Clone a virtual machine and specify the new name, storage path, and MAC address:

`virt-clone {{[-o|--original]}} {{vm_name}} {{[-n|--name]}} {{new_vm_name}} {{[-f|--file]}} {{path/to/new_storage}} {{[-m|--mac]}} {{ff:ff:ff:ff:ff:ff|RANDOM}}`
