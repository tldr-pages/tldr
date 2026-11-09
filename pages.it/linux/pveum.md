# pveum

> Gestisce gli utenti di Proxmox.
> Maggiori informazioni: <https://pve.proxmox.com/pve-docs/pveum.1.html>.

- Elenca gli utenti:

`pveum {{[u|user]}} {{[l|list]}}`

- Aggiungi un utente:

`pveum {{[u|user]}} {{[a|add]}} {{nome_utente}}@pve`

- Aggiungi un utente con email, descrizione e password:

`pveum {{[u|user]}} {{[a|add]}} {{nome_utente}}@pve --email {{indirizzo_email}} --comment {{descrizione}} --password {{password}}`

- Cambia password utente:

`pveum {{[pa|passwd]}} {{nome_utente}}@pve`

- Elimina un utente:

`pveum {{[u|user]}} {{[d|delete]}} {{nome_utente}}@pve`

- Dai a un utente accesso a una VM specifica con permessi specifici:

`pveum {{[a|acl]}} {{[m|modify]}} /vms/{{1000}} --user {{nome_utente}}@pve --role {{PVEVMUser}}`
