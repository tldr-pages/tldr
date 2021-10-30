# virsh-list

> List the ID, name, and state of virtual machines.
> See also: `virsh`.
> More information: <https://manned.org/virsh>.

- List information about running virtual machines:

`virsh list`

- List information about virtual machines regardless of state:

`virsh list --all`

- List information about virtual machines with autostart either enabled or disabled:

`virsh list --all --{{autostart|no-autostart}}`

- List information about virtual machines either with or without snapshots:

`virsh list --all --{{with-snapshot|without-snapshot}}`
