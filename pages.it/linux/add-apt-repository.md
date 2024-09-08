# add-apt-repository

> Gestisce le definizioni di repository APT.
> Maggiori informazioni: <https://manned.org/apt-add-repository>.

- Aggiunge un nuovo repository APT:

`add-apt-repository {{identificativo_del_repository}}`

- Rimuove un repository APT:

`add-apt-repository --remove {{identificativo_del_repository}}`

- Aggiorna la cache dei pacchetti dopo aver aggiunto un repository:

`add-apt-repository --update {{identificativo_del_repository}}`

- Attiva i pacchetti sorgente:

`add-apt-repository --enable-source {{identificativo_del_repository}}`
