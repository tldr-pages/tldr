# qm

> Qemu/KVM Virtual Machine Manager.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- To view a list of VMs:

`qm list`

- Using an iso file uploaded on the local storage, create a VM with a 4 GB IDE disk on the local-lvm storage:

`qm create {{100}} -ide0 {{local-lvm:4}} -net0 {{e1000}} -cdrom {{local:iso/proxmox-mailgateway_2.1.iso}}`

- Show the configuration of VM 100:

`qm config {{100}}`

- Start VM 100:

`qm start {{100}}`

- Send a shutdown request, then wait until the VM is stopped:

`qm shutdown {{100}} && qm wait {{100}}`

- Destroy a VM and remove all related resources:

`qm destroy {{100}} --purge`
