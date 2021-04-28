# virsh

> Manage virsh guest domains.
> NOTE: 'guest_id' can be the id, name or UUID of the guest.
> More information: <https://libvirt.org/virshcmdref.html>.

- Connect to a hypervisor session:

`virsh connect {{qemu:///system}}`

- List all domains:

`virsh list --all`

- Dump guest configuration file:

`virsh dumpxml {{guest_id}} > {{path/to/guest.xml}}`

- Create a guest from a configuration file:

`virsh create {{path/to/config_file.xml}}`

- Edit a guest's configuration file (editor can be changed with $EDITOR):

`virsh edit {{guest_id}}`

- Start/reboot/shutdown/suspend/resume a guest:

`virsh {{command}} {{guest_id}}`

- Save the current state of a guest to a file:

`virsh save {{guest_id}} {{filename}}`

- Delete a running guest:

`virsh destroy {{guest_id}} && virsh undefine {{guest_id}}`
