# adb

> Android Debug Bridge: comunica cu o instanță emulator Android sau dispozitive Android conectate.
> Mai multe informaţii: <https://developer.android.com/studio/command-line/adb>

- Verificați dacă procesul serverului adb rulează și porniți-l:

`adb start-server`

- Termină procesul de server adb:

`adb kill-server`

- Porniți o coajă de la distanță în instanța emulatorului/dispozitivului țintă:

`adb shell`

- Împingeți o aplicație Android la un emulator/dispozitiv:

`adb install -r {{path/to/file.apk}}`

- Copiați un fișier/director de pe dispozitivul țintă:

`adb pull {{path/to/device_file_or_directory}} {{path/to/local_destination_directory}}`

- Copiați un fișier/director pe dispozitivul țintă:

`adb push {{path/to/local_file_or_directory}} {{path/to/device_destination_directory}}`

- Obțineți o listă de dispozitive conectate:

`adb devices`
