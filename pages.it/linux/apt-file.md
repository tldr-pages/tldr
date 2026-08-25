# apt-file

> Cerca file nei pacchetti `apt`, inclusi quelli non ancora installati.
> Maggiori informazioni: <https://manned.org/apt-file>.

- Aggiorna il database dei metadati:

`sudo apt update`

- Cerca i pacchetti che contengono il file o percorso specificato:

`apt-file {{[find|search]}} {{percorso/al/file}}`

- Elenca i contenuti di un pacchetto specifico:

`apt-file list {{pacchetto}}`

- Cerca pacchetti che corrispondono a una `regex`:

`apt-file {{[find|search]}} {{[-x|--regexp]}} {{regex}}`
