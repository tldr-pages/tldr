# virsh snapshot-delete

> Delete a snapshot
> More information: <https://manned.org/virsh>.

- Delete a snapshot and merge it to its children:

`sudo virsh snapshot-delete "{{vm_name}}" "{{snapshot_name}}"`

- Delete only the metadata, leaving the snapshot contents in place.

`sudo virsh snapshot-delete "{{vm_name}}" "{{snapshot_name}}" --metadata`
