# virsh-undefine

> Delete a virtual machine.
> More information: <https://manned.org/virsh>.

- Delete only the virtual machine configuration file:

`virsh undefine --domain {{vm_name}}`

- Delete the configuration file and all associated storage volumes:

`virsh undefine --domain {{vm_name}} --remove-all-storage`

- Delete the configuration file and the specified storage volumes using the target name or the source name (as obtained from the `virsh domblklist` command):

`virsh undefine --domain {{vm_name}} --storage {{sda,path/to/source}}`
