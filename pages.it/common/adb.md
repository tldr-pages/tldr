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

`adb install -r {{percorso/del/file.apk}}`

- Copia file o cartelle dal dispositivo target:

`adb pull {{percorso/del/file_o_cartella_dispositivo}} {{percorso/del/file_o_cartella_locale}}`

- Copia file/cartelle sul dispositivo target:

`adb push {{percorso/del/file_o_cartella_locale}} {{percorso/della/cartella_destinazione_dispositivo}}`

- Mostra una lista dei dispositivi connessi:

`adb devices`
