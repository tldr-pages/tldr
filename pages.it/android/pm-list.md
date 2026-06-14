# pm list

> Elenca utenti, pacchetti, permessi, instrumentation, gruppi di permessi, funzionalità e librerie gestiti dal package manager.
> Maggiori informazioni: <https://developer.android.com/tools/adb#pm>.

- Elenca tutti i pacchetti installati:

`pm list packages`

- Elenca solo i pacchetti di [s]istema o quelli di terze parti:

`pm list packages {{-s|-3}}`

- Mostra tutti gli utenti sul sistema:

`pm list users`

- Mostra tutti i gruppi di permessi conosciuti:

`pm list permission-groups`

- Mostra tutti i permessi conosciuti:

`pm list permissions`

- Elenca tutti i pacchetti di test:

`pm list instrumentation`

- Mostra tutte le funzionalità del sistema:

`pm list features`

- Mostra tutte le librerie supportate dal dispositivo corrente:

`pm list libraries`
