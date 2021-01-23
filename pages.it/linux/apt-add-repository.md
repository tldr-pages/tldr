# apt-add-repository

> Gestisce le definizioni di repository apt.

- Aggiunge un nuovo repository apt:

`apt-add-repository {{identificativo_del_repository}}`

- Rimuove un repository apt:

`apt-add-repository --remove {{identificativo_del_repository}}`

- Aggiorna la cache dei pacchetti dopo aver aggiunto un repository:

`apt-add-repository --update {{identificativo_del_repository}}`

- Attiva i pacchetti sorgente:

`apt-add-repository --enable-source {{identificativo_del_repository}}`
