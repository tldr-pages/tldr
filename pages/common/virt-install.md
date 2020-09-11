# virt-install

> libvirt utility to create new virtual machine and run installation.
> Home page: <https://virt-manager.org/>

- Create new virtual machine and run Debian installation:

`virt-install --memory 1024 --disk path=~/image.qcow2,size=12 --cdrom {{~/debian.iso}}`
