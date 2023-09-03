# limactl

> Virtual machine manager for Linux guests, with multiple VM templates available.
> Can be used to run containers on macOS, but also for generic virtual machine use cases on macOS and Linux hosts.
> More information: <https://github.com/lima-vm/lima>.

- See available VM templates:

`limactl create --list-templates`

- Pick any of the available distributions:

`LIMA_DISTRO={{debian|fedora|ubuntu|…}}`

- Create a virtual machine using the default settings (this will download the VM image on the first run):

`limactl create {{--name=$LIMA_DISTRO-vm}} template://$LIMA_DISTRO`

- Start the VM instance (this might install some dependencies in the VM and take a few minutes):

`limactl start {{$LIMA_DISTRO-vm}}`

- Open a remote shell inside the VM:

`limactl shell {{$LIMA_DISTRO-vm}}`

- Stop/shutdown the VM instance:

`limactl stop {{$LIMA_DISTRO-vm}}`

- Delete the VM instance:

`limactl remove {{$LIMA_DISTRO-vm}}`
