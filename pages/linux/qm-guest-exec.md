# qm guest exec

> Execute a specific command via a guest agent.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Execute a specific command via a guest agent:

`qm guest exec {{vm_id}} {{command}} {{arg1 arg2 ...}}`

- Execute a specific command via a guest agent asynchronously:

`qm guest exec {{vm_id}} {{arg1 arg2 ...}} --synchronous 0`

- Execute a specific command via a guest agent with a specified timeout of 10 seconds:

`qm guest exec {{vm_id}} {{arg1 arg2 ...}} --timeout {{10}}`

- Execute a specific command via a guest agent and forward input from STDIN until EOF to the guest agent:

`qm guest exec {{vm_id}} {{arg1 arg2 ...}} --pass-stdin 1`
