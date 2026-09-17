# screencap

> Cattura uno screenshot di un display mobile.
> Questo comando può essere usato solo tramite `adb shell`.
> Maggiori informazioni: <https://developer.android.com/tools/adb#screencap>.

- Cattura uno screenshot:

`screencap {{percorso/del/file.png}}`

- Stampa il contenuto del file su `stdout` come PNG:

`screencap -p`

- Cattura uno screenshot e salvalo tramite una connessione `adb`:

`adb shell screencap -p > {{percorso/del/file.png}}`

- Mostra l'aiuto:

`screencap -h`
