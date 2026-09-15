# apt-clone

> Clona/salva/ripristina lo stato dei pacchetti di un sistema basato su Debian.
> Maggiori informazioni: <https://github.com/mvo5/apt-clone>.

- Clona lo stato dei pacchetti del sistema corrente in una directory specificata:

`apt-clone clone {{path/to/directory}}`

- Crea un file clone (`.tar.gz`) per scopi di backup:

`apt-clone clone --destination {{path/to/backup.tar.gz}}`

- Ripristina lo stato dei pacchetti da un file clone:

`apt-clone restore {{path/to/backup.tar.gz}}`

- Mostra informazioni su un file clone (es. release, architettura):

`apt-clone info {{path/to/backup.tar.gz}}`

- Verifica se il file clone può essere ripristinato sul sistema corrente:

`apt-clone restore {{path/to/backup.tar.gz}} --destination {{path/to/ripristino}}`
