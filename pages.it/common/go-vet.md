# go vet

> Controlla il codice sorgente Go e segnala costruzioni sospette (es. lint dei file sorgente Go).
> Go vet restituisce un codice di uscita non-zero se trova problemi; restituisce zero se non trova problemi.
> Maggiori informazioni: <https://pkg.go.dev/cmd/vet>.

- Controlla il pacchetto Go nella directory corrente:

`go vet`

- Controlla il pacchetto Go nel percorso specificato:

`go vet {{percorso/del/file_o_directory}}`

- Elenca i controlli disponibili che possono essere eseguiti con go vet:

`go tool vet help`

- Visualizza dettagli e flag per un controllo particolare:

`go tool vet help {{check_name}}`

- Mostra le linee offending più `n` linee di contesto circostante:

`go vet -c={{n}}`

- Output analisi ed errori in formato JSON:

`go vet -json`
