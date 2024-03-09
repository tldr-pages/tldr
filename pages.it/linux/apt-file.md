# apt-file

> Cerca un file dentro un pacchetto APT, includendo quelli non ancora installati.
> Maggiori informazioni: <https://manpages.debian.org/latest/apt-file/apt-file.1.html>.

- Aggiorna il database dei metadati:

`sudo apt update`

- Cerca i pacchetti che contengono un file o un percorso specificato:

`apt-file search {{parte/del/filename}}`

- Elenca i contenuti di un pacchetto specifico:

`apt-file list {{nome_del_pacchetto}}`
