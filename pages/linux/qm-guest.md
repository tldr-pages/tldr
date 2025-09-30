# qm guest

> Manage a VM guest agent.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Print the status of a specific PID:

`qm {{[g|guest]}} {{[exec-s|exec-status]}} {{vm_id}} {{pid}}`

- Set a password for a specific user in a virtual machine interactively:

`qm {{[g|guest]}} {{[p|passwd]}} {{vm_id}} {{username}}`

- Execute a specific QEMU Guest Agent command:

`qm {{[g|guest]}} {{[c|cmd]}} {{virtual_machine_id}} {{fsfreeze-freeze|fsfreeze-status|fsfreeze-thaw|fstrim|get-fsinfo|...}}`

- Execute a specific command via a guest agent:

`qm {{[g|guest]}} exec {{vm_id}} {{command}} {{argument1 argument2 ...}}`
