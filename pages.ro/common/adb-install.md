# adb install

> Android Debug Bridge Install: Push pachete la o instanță emulator Android sau dispozitive Android conectate.
> Mai multe informaţii: <https://developer.android.com/studio/command-line/adb>

- Împingeți o aplicație Android la un emulator/dispozitiv:

`adb install {{path/to/file.apk}}`

- Reinstalați o aplicație existentă, păstrând datele sale:

`adb install -r {{path/to/file.apk}}`

- Acordați toate permisiunile listate în manifestul aplicației:

`adb install -g {{path/to/file.apk}}`

- Actualizați rapid un pachet instalat prin actualizarea numai a părților din APK care s-au schimbat:

`adb install --fastdeploy {{path/to/file.apk}}`
