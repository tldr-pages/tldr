# pveam

> Manage LXC container templates.
> More information: <https://pve.proxmox.com/pve-docs/pveam.1.html>.

- Update container template database:

`pveam {{[u|update]}}`

- List available templates:

`pveam {{[a|available]}}`

- Download a template:

`pveam {{[d|download]}} {{local}} {{template_name}}`

- List downloaded templates:

`pveam {{[l|list]}} {{local}}`

- List available templates in a specific section:

`pveam {{[a|available]}} --section {{system|turnkeylinux|mail}}`

- Remove a template:

`pveam {{[r|remove]}} {{local}}:{{vztmpl}}/{{template_name}}`
