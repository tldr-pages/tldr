# qm resume

> Resume a virtual machine.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_resume>.

- Resume a specific virtual machine:

`qm {{[resu|resume]}} {{vm_id}}`

- Resume a specific virtual machine ignoring locks (requires root):

`sudo qm {{[resu|resume]}} {{vm_id}} --skiplock true`
