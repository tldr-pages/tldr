# qm reboot

> Reboot a virtual machine by shutting it down, and starting it again after applying pending changes.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Reboot a virtual machine:

`qm reboot {{VM_ID}}`

- Reboot a virtual machine after wait for at most 10 seconds:

`qm reboot --timeout {{10}} {{VM_ID}}`
