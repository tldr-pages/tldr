# add-apt-repository

> Gestisce le definizioni di repository apt.

- Aggiunge un nuovo repository apt:

`add-apt-repository {{identificativo_del_repository}}`

- Rimuove un repository apt:

`add-apt-repository --remove {{identificativo_del_repository}}`

- Aggiorna la cache dei pacchetti dopo aver aggiunto un repository:

`add-apt-repository --update {{identificativo_del_repository}}`

- Attiva i pacchetti sorgente:

`add-apt-repository --enable-source {{identificativo_del_repository}}`
