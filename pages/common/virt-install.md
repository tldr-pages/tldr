# virt-install

> libvirt utility to create new virtual machine and run installation.
> Home page: <https://virt-manager.org/>.

- Create a virtual machine with 1G RAM and 12G storage and run Debian installation:

`virt-install --memory {{1024}} --disk path={{~/image.qcow2}},size={{12}} --cdrom {{/path/to/file/debian.iso}}`
