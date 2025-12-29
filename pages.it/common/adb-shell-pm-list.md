# adb shell pm list

> Elenca utenti, pacchetti, permessi, instrumentation, gruppi di permessi, feature e librerie gestite dal package manager.
> Maggiori informazioni: <https://developer.android.com/tools/adb>.

- Elenca tutti i pacchetti installati:

`adb shell pm list packages`

- Stampa tutti gli utenti del sistema:

`adb shell pm list users`

- Stampa tutti i gruppi di permessi conosciuti:

`adb shell pm list permission-groups`

- Stampa tutti i permessi conosciuti:

`adb shell pm list permissions`

- Elenca tutti i pacchetti di test:

`adb shell pm list instrumentation`

- Stampa tutte le feature del sistema:

`adb shell pm list features`

- Stampa tutte le librerie supportate dal dispositivo corrente:

`adb shell pm list libraries`
