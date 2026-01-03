# virsh

> Manage `virsh` guest domains.
> Note: Some of the commands below may require specifying `virsh --connect URI` explicitly.
> Some subcommands such as `list` have their own usage documentation.
> More information: <https://libvirt.org/manpages/virsh.html>.

- Connect to a hypervisor session interactively:

`virsh {{[-c|--connect]}} {{qemu:///system|qemu:///session|xen:///system|lxc:///system|...}}`

- List all domains:

`virsh {{[-c|--connect]}} {{URI}} list --all`

- Activate a network named `default`:

`virsh net-start {{default}}`

- Create a domain from a configuration file:

`virsh create {{path/to/config_file.xml}}`

- Edit a domains's configuration file (editor can be changed with `$EDITOR` or `$VISUAL`):

`virsh edit {{domain}}`

- Start/reboot/reset/shutdown/destroy/suspend/resume a domain:

`virsh {{start|reboot|reset|shutdown|destroy|suspend|resume}} {{domain}}`

- Save the current running state of a domain (RAM, but not disk state) to a state file (domain will be powered off):

`virsh save {{domain}} {{path/to/state_file}}`

- Remove storage and snapshots of a stopped domain:

`virsh undefine {{domain}} --remove-all-storage --snapshots-metadata`
