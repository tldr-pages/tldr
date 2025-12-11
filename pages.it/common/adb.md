# adb

> Android Debug Bridge: comunica con un'istanza di un emulatore Android o con dispositivi Android connessi.
> Alcuni sottocomandi come `shell` hanno la propria documentazione di utilizzo.
> Maggiori informazioni: <https://developer.android.com/tools/adb>.

- Controlla se il processo server adb è in esecuzione e avvialo:

`adb start-server`

- Termina il processo server adb:

`adb kill-server`

- Avvia una shell remota nell'istanza dell'emulatore/dispositivo target:

`adb shell`

- Installa un'applicazione Android su un emulatore/dispositivo:

`adb install -r {{percorso/del/file.apk}}`

- Copia un file/directory dal dispositivo target:

`adb pull {{percorso/del/device_file_o_directory}} {{percorso/della/directory_di_destinazione_locale}}`

- Copia un file/directory sul dispositivo target:

`adb push {{percorso/del/file_locale_o_directory}} {{percorso/della/directory_di_destinazione_device}}`

- Elenca tutti i dispositivi connessi:

`adb devices`

- Specifica quale dispositivo deve ricevere i comandi se ci sono più dispositivi:

`adb -s {{device_ID}} {{shell}}`
