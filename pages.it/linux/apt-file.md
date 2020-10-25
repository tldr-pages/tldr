# apt-file

> Cerca un file dentro un pacchetto apt, includendo quelli non ancora installati.

- Aggiorna il database dei metadati:

`sudo apt update`

- Cerca i pacchetti che contengono un file o un percorso specificato:

`apt-file search {{parte/del/filename}}`

- Elenca i contenuti di un pacchetto specifico:

`apt-file list {{nome_del_pacchetto}}`
