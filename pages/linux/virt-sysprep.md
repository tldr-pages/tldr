# virt-sysprep

> Reset, unconfigure, or customize a virtual machine image.
> This command can be used on a virtual machine or directly on a virtual machine disk image.
> Note: You may require to use `sudo` and explicity pass `--connect URI` to the commands.
> More information: <https://libguestfs.org/virt-sysprep.1.html>.

- List all supported operations (default enabled operations are indicated with asterisks):

`virt-sysprep --list-operations`

- Run only the specified operations:

`virt-sysprep {{[-d|--domain]}} {{vm_name}} --operations {{operation1,operation2,...}}`

- Remove sensitive system data from a virtual machine image:

`virt-sysprep {{[-a|--add]}} {{path/to/image.qcow2}}`

- Specify a virtual machine by its name and run all enabled operations but don't actually apply the changes:

`virt-sysprep {{[-d|--domain]}} {{vm_name}} {{[-n|--dry-run]}}`

- Reset network interface configurations and the hostname to avoid network conflicts:

`virt-sysprep {{[-d|--domain]}} {{vm_name}} --operations machine-id,customize --hostname {{new_hostname}}`

- Set the root password for a disk image:

`virt-sysprep {{[-a|--add]}} {{path/to/image.qcow2}} --operations customize --root-password password:{{new_password}}`

- Inject a new user with a defined password and add them to the sudo group:

`virt-sysprep {{[-a|--add]}} {{path/to/image.qcow2}} --run-command 'useradd -m {{username}} && echo {{username}}:{{password}} | chpasswd && usermod -aG sudo {{username}}'`

- Install specific package(s) on a disk image (use `--update` to upgrade all installed packages to latest):

`virt-sysprep {{[-a|--add]}} {{path/to/image.qcow2}} --operations customize --network --install {{package_name1,package_name2,...}}`
