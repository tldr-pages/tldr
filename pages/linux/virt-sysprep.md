# virt-sysprep

> Reset, unconfigure, or customize a virtual machine image.
> This command can be used on a virtual machine or directly on a virtual machine disk image.
> Note: You may need to pass `--connect URI` to the commands or set up the URI in `$XDG_CONFIG_HOME/libvirt/libvirt.conf`.
> More information: <https://libguestfs.org/virt-sysprep.1.html>.

- List all supported operations (default enabled operations are indicated with asterisks):

`virt-sysprep --list-operations`

- Run only the specified operations:

`sudo virt-sysprep {{[-d|--domain]}} {{vm_name}} --operations {{operation1,operation2,...}}`

- Remove sensitive system data from a virtual machine image (operations marked as default):

`sudo virt-sysprep {{[-a|--add]}} {{path/to/image.qcow2}}`

- Specify a virtual machine by its name and run all enabled operations but don't actually apply the changes:

`sudo virt-sysprep {{[-d|--domain]}} {{vm_name}} {{[-n|--dry-run]}}`

- Reset NetworkManager network configurations, persistent MAC mappings, and the hostname to avoid network conflicts:

`sudo virt-sysprep {{[-d|--domain]}} {{vm_name}} --operations machine-id,net-hwaddr,net-hostname,net-nmconn,customize --hostname {{new_hostname}}`

- Set the root password for a disk image:

`sudo virt-sysprep {{[-a|--add]}} {{path/to/image.qcow2}} --operations customize --root-password password:{{new_password}}`

- Inject a new user with a defined password and add them to the sudo group:

`sudo virt-sysprep {{[-a|--add]}} {{path/to/image.qcow2}} --run-command 'useradd -m {{username}} && echo {{username}}:{{password}} | chpasswd && usermod -aG sudo {{username}}'`

- Install specific package(s) on a disk image (use `--update` to upgrade all installed packages to latest):

`sudo virt-sysprep {{[-a|--add]}} {{path/to/image.qcow2}} --operations customize --network --install {{package_name1,package_name2,...}}`
