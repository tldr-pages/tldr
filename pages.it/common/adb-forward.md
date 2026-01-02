# adb forward

> Inoltra le connessioni socket a un dispositivo Android o emulatore collegato.
> Maggiori informazioni: <https://developer.android.com/tools/adb>.

- Inoltra una porta TCP all'unico emulatore o dispositivo collegato:

`adb forward tcp:{{porta_locale}} tcp:{{porta_remota}}`

- Inoltra una porta TCP a un emulatore o dispositivo specifico (per ID dispositivo / numero seriale):

`adb -s {{device_ID}} forward tcp:{{porta_locale}} tcp:{{porta_remota}}`

- Elenca tutti gli inoltri:

`adb forward --list`

- Rimuove una regola di inoltro:

`adb forward --remove tcp:{{porta_locale}}`

- Rimuove tutte le regole di inoltro:

`adb forward --remove-all`
