# orb

> Interface for OrbStack, a fast and lightweight container and virtual machine runtime for macOS.
> Provides Docker-compatible commands and Linux VM management.
> More information: <https://docs.orbstack.dev/>.

- List all containers and VMs:

`orb list`

- Create and start a Linux virtual machine:

`orb create {{vm_name}}`

- Create a VM with a specific Linux distribution:

`orb create {{vm_name}} {{ubuntu|fedora|arch|debian}}`

- Start or stop a virtual machine:

`orb {{start|stop}} {{vm_name}}`

- Connect to a VM via SSH:

`orb ssh {{vm_name}}`

- Execute a command in a VM:

`orb exec {{vm_name}} {{command}}`

- Delete a virtual machine:

`orb delete {{vm_name}}`

- Show system status and resource usage:

`orb status`
