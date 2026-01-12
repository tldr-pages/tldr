# adb connect

> Connettiti a un dispositivo Android in modalità wireless.
> Maggiori informazioni: <https://developer.android.com/tools/adb>.

- Abbina con un dispositivo Android (indirizzo e codice di accoppiamento si trovano nelle opzioni sviluppatore):

`adb pair {{indirizzo_ip}}:{{porta}}`

- Connettiti a un dispositivo Android (la portaa sarà diversa dall'accoppiamento):

`adb connect {{indirizzo_ip}}:{{porta}}`

- Disconnetti un dispositivo:

`adb disconnect {{indirizzo_ip}}:{{porta}}`
