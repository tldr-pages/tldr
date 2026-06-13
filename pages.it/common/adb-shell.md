# adb shell

> Android Debug Bridge Shell: Esegue un commando remoto sull'emulatore o dispositivo Android connesso.
> Maggiori informazioni: <https://developer.android.com/tools/adb>.

- Avvia un interprete di comandi iterativo remoto sull'emulatore/dispositivo:

`adb shell`

- Fornisce tutte le proprietà dell'emulatore o dispositivo:

`adb shell getprop`

- Ripristina tutti i permessi di esecuzione ai loro valori predefiniti:

`adb shell pm reset-permissions`

- Revoca un permesso pericoloso da un'applicazione:

`adb shell pm revoke {{pacchetto}} {{permesso}}`

- Attiva un evento chiave:

`adb shell input keyevent {{keycode}}`

- Pulisce i dati di un'applicazione sull'emulatore o dispositivo:

`adb shell pm clear {{pacchetto}}`

- Avvia un'attività sull'emulatore/dispositivo:

`adb shell am start -n {{pacchetto}}/{{attività}}`

- Avvia la schermata iniziale sull'emulatore o dispositivo:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
