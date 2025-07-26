# qm disk resize

> Resize a virtual machine disk in the Proxmox Virtual Environment (PVE).
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Add `n` gigabytes to a virtual disk:

`qm {{[di|disk]}} resize {{vm_id}} {{disk_name}} +{{n}}G`
