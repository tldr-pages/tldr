# clamscan

> Scanner antivirus da linea di comando.
> Maggiori informazioni: <https://docs.clamav.net/manual/Usage/Scanning.html#clamscan>.

- Analizza un file cercando vulnerabilità:

`clamscan {{percorso/del/file}}`

- Analizza ricorsivamente tutti i file in una specifica directory:

`clamscan {{[-r|--recursive]}} {{percorso/della/directory}}`

- Analizza dati da `stdin`:

`{{comando}} | clamscan -`

- Specifica un file o directory di file da usare come database virus:

`clamscan {{[-d|--database]}} {{percorso/del/file_o_directory}}`

- Analizza la directory corrente e mostra in output solo i file infetti:

`clamscan {{[-i|--infected]}}`

- Scrivi il risultato di uno scan in un file di log:

`clamscan {{[-l|--log]}} {{percorso/del/file_log}}`

- Sposta i file infetti in una specifica directory:

`clamscan --move {{percorso/della/directory_quarantena}}`

- Elimina i file infetti:

`clamscan --remove yes`
