# winget

> Gestore pacchetti a linea di comando di Windows.
> Maggiori informazioni: <https://learn.microsoft.com/windows/package-manager/winget>.

- Installa un pacchetto:

`winget install {{pacchetto}}`

- Mostra informazioni su un pacchetto:

`winget show {{pacchetto}}`

- Cerca un pacchetto:

`winget search {{pacchetto}}`

- Aggiorna tutti i pacchetti all'ultima versione:

`winget upgrade --all`

- Elenca tutti i pacchetti installati che possono essere gestiti con winget:

`winget list --source winget`
