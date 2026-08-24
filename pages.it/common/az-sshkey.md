# az sshkey

> Gestisce le chiavi pubbliche SSH con le macchine virtuali.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/sshkey>.

- Crea una nuova chiave SSH:

`az sshkey create --name {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}}`

- Carica una chiave SSH esistente:

`az sshkey create --name {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}} --public-key "{{@percorso/verso/chiave.pub}}"`

- Elenca tutte le chiavi pubbliche SSH:

`az sshkey list`

- Mostra informazioni su una chiave pubblica SSH:

`az sshkey show --name {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}}`
