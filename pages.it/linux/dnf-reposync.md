# dnf reposync

> Sincronizza pacchetti e metadata di un repository DNF remoto in una directory locale.
> Non predefinito in `dnf` ma supportato tramite `dnf-plugins-core`.
> Vedi anche: `dnf`.
> Maggiori informazioni: <https://dnf-plugins-core.readthedocs.io/en/latest/reposync.html>.

- Sincronizza tutti i pacchetti dal repository con id `repo_name` in una sottodirectory `repo_name` della directory di lavoro corrente:

`dnf reposync --repoid {{repo_name}}`

- Sincronizza tutti i pacchetti e definisce una posizione di salvataggio personalizzata:

`dnf reposync --repoid {{repo_name}} {{[-p|--download-path]}} {{path/to/directory}}`

- Sincronizza tutti i pacchetti e metadati:

`dnf reposync --repoid {{repo_name}} --download-metadata`

- Scarica solo i pacchetti più recenti per repository:

`dnf reposync --repoid {{repo_name}} {{[-n|--newest-only]}}`

- Mostra solo gli URL di ciò che verrebbe scaricato, non scaricare:

`dnf reposync --repoid {{repo_name}} {{[-u|--urls]}}`

- Tenta di impostare i timestamp dei file scaricati su quelli del lato remoto:

`dnf reposync --repoid {{repo_name}} --remote-time`
