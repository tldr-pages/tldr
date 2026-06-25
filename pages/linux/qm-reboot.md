# qm reboot

> Reboot a virtual machine by shutting it down, and starting it again after applying pending changes.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_reboot>.

- Reboot a virtual machine:

`qm {{[reb|reboot]}} {{100}}`

- Reboot a virtual machine after wait for at most 10 seconds:

`qm {{[reb|reboot]}} {{100}} --timeout {{10}}`
