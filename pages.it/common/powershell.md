# powershell

> Shell della riga di comando e linguaggio di scripting progettato appositamente per l'amministrazione dei sistemi.
> Guarda anche: `pwsh`.
> Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/powershell>.

- Avvia una sessione di shell interattiva:

`powershell`

- Avvia una sessione shell interattiva senza caricare le configurazioni di avvio:

`powershell -NoProfile`

- Esegui specifici comandi:

`powershell -Command "{{echo 'powershell è eseguito'}}"`

- Esegui uno specifico script:

`powershell -File {{percorso/dello/script.ps1}}`

- Avvia una sessione con una versione specifica di PowerShell:

`powershell -Version {{versione}}`

- Impedisci l'uscita dalla shell dopo aver eseguito i comandi di avvio:

`powershell -NoExit`

- Specifica il formato dei dati inviati a PowerShell:

`powershell -InputFormat {{Text|XML}}`

- Specifica come formattatare l'output da PowerShell:

`powershell -OutputFormat {{Text|XML}}`
