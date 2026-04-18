# qm showcmd

> Show command-line which is used to start the VM (debug info).
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_showcmd>.

- Show command-line for a specific virtual machine:

`qm {{[sho|showcmd]}} {{100}}`

- Put each option on a new line to enhance human readability:

`qm {{[sho|showcmd]}} --pretty {{true}} {{100}}`

- Fetch configuration values from a specific snapshot:

`qm {{[sho|showcmd]}} --snapshot {{string}} {{100}}`
