# apt-file

> Cerca un file dentro un pacchetto APT, includendo quelli non ancora installati.
> Maggiori informazioni: <https://manned.org/apt-file.1>.

- Aggiorna il database dei metadati:

`sudo apt update`

- Cerca i pacchetti che contengono un file o un percorso specificato:

`apt-file {{search|find}} {{parte/del/filename}}`

- Elenca i contenuti di un pacchetto specifico:

`apt-file {{show|list}} {{nome_del_pacchetto}}`
