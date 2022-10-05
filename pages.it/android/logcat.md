# logcat

> Scarica il registro dei messaggi di sistema, comprese le _stack traces_ quando si verifica un errore, e i messaggi di log delle applicazioni.
> Informazioni aggiuntive: <https://developer.android.com/studio/command-line/logcat>.

- Mostra il log di sistema:

`logcat`

- Scrivi il log di sistema su file:

`logcat -f {{percorso/al/file}}`

- Mostra le righe corrispondenti ad una specifica _regular expression_:

`logcat --regex {{regular_expression}}`
