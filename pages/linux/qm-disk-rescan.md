# qm disk rescan

> Rescan all storages and update disk sizes and unused disk images of virtual machines.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Rescan all storages and update disk sizes and unused disk images:

`qm {{[di|disk]}} {{[resc|rescan]}}`

- Perform a dry-run of a rescan and do not write any changes to configurations:

`qm {{[di|disk]}} {{[resc|rescan]}} --dryrun`

- Specify a virtual machine by its ID:

`qm {{[di|disk]}} {{[resc|rescan]}} --vmid {{100}}`
