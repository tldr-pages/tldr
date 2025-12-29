# adb install

> Android Debug Bridge Install: Invia pacchetti ad un emulatore Android od ad un dispositivo Android connesso.
> Maggiori informazioni: <https://developer.android.com/tools/adb>.

- Invia un'applicazione Android ad un emulatore/dispositivo:

`adb install {{percorso/del/file.apk}}`

- Invia un'applicazione Android ad un emulatore/dispositivo specifico (sovrascrive `$ANDROID_SERIAL`):

`adb -s {{serial_number}} install {{percorso/del/file.apk}}`

- [r]einstalla una applicazione esistente, preservandone i dati:

`adb install -r {{percorso/del/file.apk}}`

- Invia un'applicazione Android consentendo [d]owngrade del codice versione (solo pacchetti debuggabili):

`adb install -d {{percorso/del/file.apk}}`

- [g]rantisce tutti i permessi elencati nel manifest dell'applicazione:

`adb install -g {{percorso/del/file.apk}}`

- Aggiorna rapidamente un pacchetto installato aggiornando solamente le parti dell'APK che sono cambiate:

`adb install --fastdeploy {{percorso/del/file.apk}}`
