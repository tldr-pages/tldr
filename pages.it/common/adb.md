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

`adb install -r {{path/to/file.apk}}`

- Copia un file/directory dal dispositivo target:

`adb pull {{path/to/device_file_or_directory}} {{path/to/local_destination_directory}}`

- Copia un file/directory sul dispositivo target:

`adb push {{path/to/local_file_or_directory}} {{path/to/device_destination_directory}}`

- Elenca tutti i dispositivi connessi:

`adb devices`

- Specifica quale dispositivo deve ricevere i comandi se ci sono più dispositivi:

`adb -s {{device_ID}} {{shell}}`
