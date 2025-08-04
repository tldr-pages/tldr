# qm disk rescan

> Rescan all storages and update disk sizes and unused disk images of a virtual machine.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Rescan all storages and update disk sizes and unused disk images of a specific virtual machine:

`qm disk rescan {{vm_id}}`

- Perform a dry-run of rescan on a specific virtual machine and do not write any changes to configurations:

`qm disk rescan --dryrun {{true}} {{vm_id}}`
