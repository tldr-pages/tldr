# limactl

> Virtual machine manager for Linux guests, with multiple VM templates available.
> Can be used to run containers on macOS, but also for generic virtual machine use cases on macOS and Linux hosts.
> More information: <https://github.com/lima-vm/lima>.

- See available VM templates:

`limactl create --list-templates`

- Create a virtual machine using the default settings with any of the templates and optionally provide a name (this will download the VM image on the first run):

`limactl create {{--name=default}} template://{{debian|fedora|ubuntu|…}}`

- Start the VM instance (this might install some dependencies in the VM and take a few minutes):

`limactl start {{debian|fedora|ubuntu|…}}`

- Open a remote shell inside the VM:

`limactl shell {{debian|fedora|ubuntu|…}}`

- Stop/shutdown the VM instance:

`limactl stop {{debian|fedora|ubuntu|…}}`

- Delete the VM instance:

`limactl remove {{debian|fedora|ubuntu|…}}`
