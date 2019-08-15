# virsh

> Manage virsh guest domains.
> More information: <https://libvirt.org/virshcmdref.html>.
> NOTE: The GuestID can be the id, name or UUID of the guest.

- Connect to a hypervisor session:

`virsh connect {{qemu://system}}`

- List all domains:

`virsh list --all`

- Dump guest configuration file:

`virsh dumpxl {{GuestID}} > {{guest.xml}}`

- Create a guest from a configuration file:

`virsh create {{config_file.xml}}`

- Edit a guest's configuration file (editor can be changed with $EDITOR):

`virsh edit {{GuestID}}`

- Start/reboot/shutdown/suspend/resume a guest:

`virsh {{command}} {{GuestID}}`

- Save the current state of a guest to a file:

`virsh save {{GuestID}} {{filename}}`

- Delete a running guest:

`virsh detroy {{GuestID}} && virsh undefine {{GuestID}}`
