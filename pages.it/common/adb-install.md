# adb install

> Android Debug Bridge Install: Invia pacchetti ad un emulatore Android od ad un dispositivo Android connesso.
> Maggiori informazioni: <https://developer.android.com/studio/command-line/adb>.

- Invia un'applicazione Android ad un emulatore emulatore/Android:

`adb install {{percorso/al/file.apk}}`

- Reinstalla una applicazione esistente, preservandone i dati:

`adb install -r {{percorso/al/file.apk}}`

- Fornisce tutti i permessi elencati nel manifest dell'applicazione:

`adb install -g {{percorso/al/file.apk}}`

- Aggiorna rapidamente un pacchetto installato aggiornando solamente le parti dell'APK che sono cambiate:

`adb install --fastdeploy {{percorso/al/file.apk}}`
