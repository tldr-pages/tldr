# qm cloudinit

> Configure cloudinit settings for virtual machines managed by Proxmox Virtual Environment (PVE).
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Configure cloudinit settings for a specific user and set password for the user:

`qm {{[clou|cloudinit]}} {{vm_id}} -user={{user}} -password={{password}}`

- Configure cloudinit settings for a specific user and set password for the user with a specific SSH key:

`qm {{[clou|cloudinit]}} {{vm_id}} -user={{user}} -password={{password}} -sshkey={{ssh_key}}`

- Set the hostname for a specific virtual machine:

`qm {{[clou|cloudinit]}} {{vm_id}} -hostname={{hostname}}`

- Configure the network interface settings for a specific virtual machine:

`qm {{[clou|cloudinit]}} {{vm_id}} -ipconfig {{ipconfig}}`

- Configure a shell script to execute before `cloudinit` is run on a virtual machine:

`qm {{[clou|cloudinit]}} {{vm_id}} -pre {{script}}`
