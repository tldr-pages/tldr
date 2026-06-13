# qm wait

> Wait until the virtual machine is stopped.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_wait>.

- Wait until the virtual machine is stopped:

`qm {{[w|wait]}} {{100}}`

- Wait until the virtual machine is stopped with a 10 second timeout:

`qm {{[w|wait]}} {{100}} --timeout {{10}}`

- Send a shutdown request, then wait until the virtual machine is stopped with a 10 second timeout:

`qm {{[shu|shutdown]}} {{100}} && qm {{[w|wait]}} {{100}} --timeout {{10}}`
