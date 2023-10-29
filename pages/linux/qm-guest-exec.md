# qm guest exec

> Execute a specific command via a guest agent.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Execute a specific command via a guest agent:

`qm guest exec {{vm_id}} {{command}} {{argument1 argument2 ...}}`

- Execute a specific command via a guest agent asynchronously:

`qm guest exec {{vm_id}} {{argument1 argument2 ...}} --synchronous 0`

- Execute a specific command via a guest agent with a specified timeout of 10 seconds:

`qm guest exec {{vm_id}} {{argument1 argument2...}} --timeout {{10}}`

- Execute a specific command via a guest agent and forward input from STDIN until EOF to the guest agent:

`qm guest exec {{vm_id}} {{argument1 argument2 ...}} --pass-stdin 1`
