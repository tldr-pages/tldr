# lima

> Virtual machine manager for linux guests, with multiple vm templates available.
> Can be used to run containers on macos, but also for generic virtual machine use-cases on macos and linux hosts.
> More information: <https://github.com/lima-vm/lima>.

- Pick any of the available distributions, see templates in `/usr/local/share/lima/templates/`

`LIMA_DISTRO=debian|fedora|ubuntu|…`

- Create a virtual machine using the default settings (this will download the vm image on the first run)

`cat /usr/local/share/lima/templates/$LIMA_DISTRO.yaml | limactl create --name=$LIMA_DISTRO-vm -`

- Start the vm instance (this might install some dependencies in the vm and take a few minutes)

`limactl start $LIMA_DISTRO-vm`

- Open a remote shell inside the VM

`limactl shell $LIMA_DISTRO-vm`

- Stop/shutdown the vm instance

`limactl stop $LIMA_DISTRO-vm`

- Delete the vm instance

`limactl remove $LIMA_DISTRO-vm`
