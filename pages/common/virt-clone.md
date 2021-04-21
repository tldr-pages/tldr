# virt-clone

> Clone a libvirt virtual machine.
> More information: <https://virt-manager.org/>.

- Clone a virtual machine generating a new virtual machine name and storage path from the original name and path, and a random MAC address:

`virt-clone --original {{vm_name}} --auto-clone --mac RANDOM`
