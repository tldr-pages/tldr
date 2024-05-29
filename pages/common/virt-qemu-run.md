# virt-qemu-run

> Experimental tool to run a QEMU Guest VM independent of libvirtd.
> More information: <https://manned.org/man/virt-qemu-run>

- Run a QEMU virtual machine:

`virt-qemu-run {{path/to/guest.xml}}`

- Run a QEMU virtual machine and store the state in a specified directory:

`virt-qemu-run --root={{path/to/directory}} {{path/to/guest.xml}}`

- Run a QEMU virtual machine and display verbose information about startup:

`virt-qemu-run --verbose {{path/to/guest.xml}}`

- Display help:

`virt-qemu-run --help`
