# bash

> Bourne-Again SHell.
> Interprete da linea di comando compatibile con `sh`.
> Maggiori informazioni: <https://www.gnu.org/software/bash/>.

- Avvia una shell interattiva:

`bash`

- Esegui un comando:

`bash -c "{{comando}}"`

- Esegui dei comandi da un file:

`bash {{file.sh}}`

- Esegui dei comandi da un file, loggando tutti i comandi eseguiti nel terminale:

`bash -x {{file.sh}}`

- Esegui comandi da standard input:

`bash -s`

- Stampa informazioni sulla versione di Bash (usa `echo $BASH_VERSION` per mostrare solo la versione):

`bash --version`
