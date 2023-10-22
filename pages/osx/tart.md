# tart

> Build, run and manage macOS and Linux virtual machines (VMs) on Apple Silicon.
> More information: <https://github.com/cirruslabs/tart>.

- Pull a remote VM image:

`tart pull {{acme.io/org/name:tag}}`

- Clone a VM from a local or remote image source:

`tart clone {{source-vm}} {{vm-name}}`

- Create a new Mac VM from a specific ipsw file:

`tart create --from-ipsw={{latest|path/to/file.ipsw}} {{vm-name}}`

- Run an existing VM:

`tart run {{vm-name}}`

- Run an existing VM with a specific mounted directory:

`tart run --dir={{path/to/directory}}:{{/path/to/local_directory}} {{vm-name}}`

- List VMs:

`tart list`

- Get IP address of a running VM:

`tart ip {{vm-name}}`

- Change a VM's display resolution:

`tart set {{vm-name}} --display {{640}}x{{400}}`
