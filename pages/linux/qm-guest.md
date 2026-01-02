# qm guest

> Manage a VM guest agent.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_guest_cmd>.

- Print the status of a specific PID:

`qm {{[g|guest]}} {{[exec-s|exec-status]}} {{vm_id}} {{pid}}`

- Set a password for a specific user in a virtual machine interactively:

`qm {{[g|guest]}} {{[p|passwd]}} {{vm_id}} {{username}}`

- Set an already hashed password for a specific user in a virtual machine interactively:

`qm {{[g|guest]}} {{[p|passwd]}} {{vm_id}} {{username}} --crypted 1`

- Execute a specific QEMU Guest Agent command:

`qm {{[g|guest]}} {{[c|cmd]}} {{virtual_machine_id}} {{fsfreeze-freeze|fsfreeze-status|fsfreeze-thaw|fstrim|get-fsinfo|...}}`

- Execute a specific command via a guest agent:

`qm {{[g|guest]}} exec {{vm_id}} {{command}} {{argument1 argument2 ...}}`

- Execute a specific command via a guest agent asynchronously:

`qm {{[g|guest]}} exec {{vm_id}} {{argument1 argument2 ...}} --synchronous 0`

- Execute a specific command via a guest agent with a specified timeout of 10 seconds:

`qm {{[g|guest]}} exec {{vm_id}} {{argument1 argument2...}} --timeout {{10}}`

- Execute a specific command via a guest agent and forward input from `stdin` until EOF to the guest agent:

`qm {{[g|guest]}} exec {{vm_id}} {{argument1 argument2 ...}} --pass-stdin 1`
