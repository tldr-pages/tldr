# pct set

> Imposta le opzioni del container.
> Maggiori informazioni: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_set>.

- Imposta l'avvio automatico del container all'accensione:

`pct set {{100}} --onboot`

- Imposta un IP statico per un container:

`pct set {{100}} --net0 name=eth0,bridge=vmbr0,ip={{10.0.0.100/24}},gw={{10.0.0.1}}`

- Imposta il limite di memoria e CPU del container:

`pct set {{100}} --memory {{8192}} --cpulimit {{4}}`

- Imposta l'hostname di un container:

`pct set {{100}} --hostname {{nuovo_nome}}`

- Monta una posizione del filesystem host in un guest:

`pct set {{100}} --mp{{0}} /{{percorso/alla/directory_host}},mp=/{{percorso/al/punto_mount_guest}}`

- Imposta i tag del container:

`pct set {{100}} --tags {{tag1,tag2,...}}`

- Rimuovi un'opzione:

`pct set {{100}} --delete {{net0,mp0,mp1,...}}`
