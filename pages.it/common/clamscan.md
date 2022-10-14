# clamscan

> Scanner antivirus da linea di comando.
> Maggiori informazioni: <https://www.clamav.net>.

- Analizza un file cercando vulnerabilità:

`clamscan {{percorso/del/file}}`

- Analizza ricorsivamente tutti i file in una specifica cartella:

`clamscan -r {{percorso/alla/cartella}}`

- Analizza dati da standard input:

`{{comando}} | clamscan -`

- Specifica un file o cartella di file da usare come database virus:

`clamscan --database {{percorso/a/file_o_cartella}}`

- Analizza la cartella corrente e mostra in output solo i file infetti:

`clamscan --infected`

- Scrivi il risultato di uno scan in un file di log:

`clamscan --log {{percorso/a/file_log}}`

- Sposta i file infetti in una specifica cartella:

`clamscan --move {{percorso/a/cartella_quarantena}}`

- Elimina i file infetti:

`clamscan --remove yes`
