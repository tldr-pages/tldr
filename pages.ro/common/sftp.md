# sftp

> Program de transfer de fișiere securizat.
> Program interactiv pentru a copia fișiere între gazde prin SSH.
> Pentru transferurile de fișiere neinteractive, consultați `scp` sau `rsync`.

- Conectați-vă la un server de la distanță și introduceți un mod de comandă interactiv:

`sftp {{remote_user}}@{{remote_host}}`

- Conectați-vă folosind un port alternativ:

`sftp -P {{remote_port}} {{remote_user}}@{{remote_host}}`

- Transferați fișierul la distanță în sistemul local:

`get {{/path/remote_file}}`

- Transferați fișierul local în sistemul de la distanță:

`put {{/path/local_file}}`

- Transferați directorul de la distanță către sistemul local recursiv (funcționează și cu `put'):

`get -R {{/path/remote_directory}}`

- Obține lista de fișiere pe mașină locală:

`lls`

- Obține lista de fișiere pe mașină de la distanță:

`ls`
