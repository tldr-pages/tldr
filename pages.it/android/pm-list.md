# pm list

> Elenca utenti, pacchetti, permessi, instrumentation, gruppi di permessi, feature e librerie gestite dal package manager.
> Maggiori informazioni: <https://developer.android.com/tools/adb#pm>.

- Elenca tutti i pacchetti installati:

`pm list packages`

- Elenca solo i pacchetti di [s]istema o quelli di terze parti:

`pm list packages {{-s|-3}}`

- Stampa tutti gli utenti del sistema:

`pm list users`

- Stampa tutti i gruppi di permessi conosciuti:

`pm list permission-groups`

- Stampa tutti i permessi conosciuti:

`pm list permissions`

- Elenca tutti i pacchetti di test:

`pm list instrumentation`

- Stampa tutte le feature del sistema:

`pm list features`

- Stampa tutte le librerie supportate dal dispositivo corrente:

`pm list libraries`
