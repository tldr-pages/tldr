# virsh snapshot-list

> List available snapshots.
> More information: <https://manned.org/virsh>.

- List all snapshots and their basic information:

`sudo virsh snapshot-list "{{vm_name}}"`

- List all snapshots in a tree structure:

`sudo virsh snapshot-list "{{vm_name}}" --tree`

- Display help:

`virsh snapshot-list --help`
