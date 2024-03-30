# vboxmanage-import

> Import a previously exported virtual machine (VM).
> More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-import>.

- Import a VM from an OVF or OVA file:

`VBoxManage import {{path/to/file.ovf}}`

- Set the name of the imported VM:

`VBoxManage import {{path/to/file.ovf}} --name {{vm_name}}`

- Indicate the folder where the configuration of the imported VM will be stored:

`VBoxManage import {{path/to/file.ovf}} --basefolder {{path/to/directory}}`

- Register the imported VM in VirtualBox:

`VBoxManage import {{path/to/file.ovf}} --register`

- Perform a dry run to check the import without actually importing:

`VBoxManage import {{path/to/file.ovf}} --dry-run`

- Set the guest OS type (one of `VBoxManage list ostypes`) for the imported VM:

`VBoxManage import {{path/to/file.ovf}} --ostype={{ostype}}`

- Set the memory (in megabytes) for the imported VM:

`VBoxManage import {{path/to/file.ovf}} --memory={{1}}`

- Set the number of CPUs for the imported VM:

`VBoxManage import {{path/to/file.ovf}} --cpus={{1}}`
