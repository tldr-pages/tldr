# qm suspend

> Suspends a virtual machine (VM) in the Proxmox Virtual Environment (PVE).
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Suspend virtual machine by id:

`qm suspend -{id} 101`

- To skips the lock check when suspending the VM. Use with caution, as it may lead to data corruption in certain situations:

`qm suspend --vmid 101 --skiplock`

- To skips the lock check for storage when suspending the VM. Use with caution, as it may lead to data corruption in certain situations:

`qm suspend --vmid 101 --skiplockstorage`
