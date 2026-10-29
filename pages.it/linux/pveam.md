# pveam

> Gestisce i template dei container LXC.
> Maggiori informazioni: <https://pve.proxmox.com/pve-docs/pveam.1.html>.

- Aggiorna il database dei template dei container:

`pveam {{[u|update]}}`

- Elenca i template disponibili:

`pveam {{[a|available]}}`

- Scarica un template:

`pveam {{[d|download]}} {{local}} {{nome_template}}`

- Elenca i template scaricati:

`pveam {{[l|list]}} {{local}}`

- Elenca i template disponibili in una sezione specifica:

`pveam {{[a|available]}} --section {{system|turnkeylinux|mail}}`

- Rimuovi un template:

`pveam {{[r|remove]}} {{local}}:{{vztmpl}}/{{nome_template}}`
