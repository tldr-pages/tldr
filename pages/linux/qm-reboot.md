# qm reboot

> Reboot a virtual machine by shutting it down, and starting it again after applying pending changes.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Reboot a virtual machine:

`qm {{[reb|reboot]}} {{vm_id}}`

- Reboot a virtual machine after wait for at most 10 seconds:

`qm {{[reb|reboot]}} --timeout {{10}} {{vm_id}}`
