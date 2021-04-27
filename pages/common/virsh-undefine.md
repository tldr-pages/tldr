# virsh-undefine

> Delete a virtual machine.
> More information: <https://manned.org/virsh>.

- Delete only the virtual machine configuration file:

`virsh undefine --domain {{vm_name}}`

- Delete the configuration file and all associated storage volumes:

`virsh undefine --domain {{vm_name}} --remove-all-storage`

- Delete the configuration file and the specified storage volumes:

`virsh undefine --domain {{vm_name}} --storage {{target_name1|path/to/storage1,target_name2|path/to/storage2,...}}`
