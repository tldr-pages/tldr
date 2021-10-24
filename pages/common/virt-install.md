# virt-install

> Create virtual machines with libvirt and begin OS installation.
> More information: <https://virt-manager.org/>.

- Create a virtual machine with 1 GiB RAM and 12 GiB storage and start Debian installation:

`virt-install --name {{vm_name}} --memory {{1024}} --disk path={{path/to/image.qcow2}},size={{12}} --cdrom {{path/to/debian.iso}}`
