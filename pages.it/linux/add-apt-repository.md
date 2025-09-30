# add-apt-repository

> Gestisce le definizioni di repository APT.
> Maggiori informazioni: <https://manned.org/add-apt-repository>.

- Aggiunge un nuovo repository APT:

`add-apt-repository {{identificativo_del_repository}}`

- Rimuove un repository APT:

`add-apt-repository {{[-r|--remove]}} {{identificativo_del_repository}}`

- Aggiorna la cache dei pacchetti dopo aver aggiunto un repository:

`add-apt-repository --update {{identificativo_del_repository}}`

- Attiva i pacchetti sorgente:

`add-apt-repository {{[-s|--enable-source]}} {{identificativo_del_repository}}`
