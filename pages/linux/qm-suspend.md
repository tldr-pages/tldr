# qm suspend

> Suspends a virtual machine (VM) in the Proxmox Virtual Environment (PVE).
> Use `--skiplock` and `--skiplockstorage` flags with caution, as they may lead to data corruption in certain situations.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Suspend a virtual machine by ID:

`qm suspend {{vm_id}} {{integer}}`

- Skip the lock check when suspending the VM:

`qm suspend {{vm_id}} {{integer}} --skiplock`

- Skip the lock check for storage when suspending the VM:

`qm suspend {{vm_id}} {{integer}} --skiplockstorage`
