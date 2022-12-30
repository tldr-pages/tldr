# blackfire

> Strumento di profilazione da linea di comando per PHP.
> Maggiori informazioni: <https://blackfire.io>.

- Inizializza e configura il client Blackfire:

`blackfire config`

- Lancia l'agent Blackfire:

`blackfire agent`

- Lancia l'agent Blackfire su uno specifico socket:

`blackfire agent --socket="{{tcp://127.0.0.1:8307}}"`

- Lancia il profiler su uno specifico programma:

`blackfire run {{php percorso/del/file.php}}`

- Lancia il profiler e raccogli 10 campioni:

`blackfire --samples={{10}} run {{php percorso/del/file.php}}`

- Lancia il profiler e mostra i risultati in output come JSON:

`blackfire --json run {{php percorso/del/file.php}}`

- Carica un file del profiler sul servizio web di Blackfire:

`blackfire upload {{percorso/del/file}}`

- Mostra lo stato dei profili sul servizio web di Blackfire:

`blackfire status`
