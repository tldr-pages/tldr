# adb

> Android Debug Bridge: comunica con un'instanza di un emulatore Android o con un dispositivo android connesso.
> Alcuni comandi aggiuntivi, come `adb shell`, hanno la propria documentazione.
> Maggiori informazioni: <https://developer.android.com/studio/command-line/adb>.

- Controlla se il processo server adb è attivo ed avvialo:

`adb start-server`

- Termina il processo server adb:

`adb kill-server`

- Avvia una shell remota nell'emulatore o dispositivo target:

`adb shell`

- Installa un'applicazione Android nell'emulatore o dispositivo target:

`adb install -r {{percorso/al/file.apk}}`

- Copia file o directory dal dispositivo target:

`adb pull {{percorso/a/file_o_directory_dispositivo}} {{percorso/a/file_o_directory_locale}}`

- Copia file/directory sul dispositivo target:

`adb push {{percorso/a/file_o_directory_locale}} {{percorso/a/directory_destinazione_dispositivo}}`

- Mostra una lista dei dispositivi connessi:

`adb devices`
