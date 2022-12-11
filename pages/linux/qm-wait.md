# qm wait

> Wait until the virtual machine is stopped.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Wait until the virtual machine is stopped:

`qm wait {{vm_id}}`

- Wait until the virtual machine is stopped with a 10 second timeout:

`qm wait --timeout {{10}} {{vm_id}}`

- Send a shutdown request, then wait until the virtual machine is stopped with a 10 second timeout:

`qm shutdown {{vm_id}} && qm wait --timeout {{10}} {{vm_id}}`
