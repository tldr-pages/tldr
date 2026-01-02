# qm wait

> Wait until the virtual machine is stopped.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_wait>.

- Wait until the virtual machine is stopped:

`qm {{[w|wait]}} {{vm_id}}`

- Wait until the virtual machine is stopped with a 10 second timeout:

`qm {{[w|wait]}} --timeout {{10}} {{vm_id}}`

- Send a shutdown request, then wait until the virtual machine is stopped with a 10 second timeout:

`qm {{[shu|shutdown]}} {{vm_id}} && qm {{[w|wait]}} --timeout {{10}} {{vm_id}}`
