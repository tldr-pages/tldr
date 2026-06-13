# logcat

> Scarica un registro di messaggi di sistema, comprese le stack traces quando si verifica un errore e i messaggi di informazioni di log dalle applicazioni.
> Maggiori informazioni: <https://developer.android.com/tools/logcat>.

- Visualizza i log di sistema:

`logcat`

- Scrivi i log di sistema in un [f]ile:

`logcat -f {{percorso/al/file}}`

- Visualizza le linee che corrispondono a un `regex`:

`logcat --regex {{regex}}`

- Visualizza i log per uno specifico PID:

`logcat --pid {{pid}}`

- Visualizza i log per il processo di uno specifico pacchetto:

`logcat --pid $(pidof -s {{package}})`
