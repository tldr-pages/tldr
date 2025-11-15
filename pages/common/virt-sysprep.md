# virt-sysprep

> Reset, unconfigure, or customize a virtual machine image.
> More information: <https://manned.org/virt-sysprep>.

- List all supported operations (enabled operations are indicated with asterisks):

`virt-sysprep --list-operations`

- Remove sensitive system data from a virtual machine image:

`sudo virt-sysprep {{[-a|--add]}} {{path/to/image.qcow2}}`

- Specify a virtual machine by its name and run all enabled operations but don't actually apply the changes:

`sudo virt-sysprep {{[-d|--domain]}} {{vm_name}} {{[-n|--dry-run]}}`

- Run only the specified operations:

`sudo virt-sysprep {{[-d|--domain]}} {{vm_name}} --operations {{operation1,operation2,...}}`

- Generate a new `/etc/machine-id` file and enable customizations to be able to change the host name to avoid network conflicts:

`sudo virt-sysprep {{[-d|--domain]}} {{vm_name}} --enable {{customizations}} --hostname {{host_name}} --operation {{machine-id}}`

- Display help:

`virt-sysprep {{[-he|--help]}}`
