# tasklist

> Mostra una lista dei processi in esecuzione su una macchina locale o remota.
> Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/tasklist>.

- Mostra i processi in esecuzione:

`tasklist`

- Mostra i processi in esecuzione in un formato specifico:

`tasklist /fo {{table|list|csv}}`

- Mostra i processi in esecuzione utilizzando il nome del file `.exe` o `.dll` specificato:

`tasklist /m {{pattern_di_moduli}}`

- Mostra i processi in esecuzione su una macchina remota:

`tasklist /s {{nome_macchina_remota}} /u {{nome_utente}} /p {{password}}`

- Visualizzare i servizi utilizzando ogni processo:

`tasklist /svc`
