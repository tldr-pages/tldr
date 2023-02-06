# adb install

> Android Debug Bridge telepítése: Csomagok küldése egy Android emulátor példányra vagy csatlakoztatott Android eszközökre. További információ: <https://developer.android.com/studio/command-line/adb>.

- Android-alkalmazás tolása egy emulátorra/készülékre:

`adb install {{path/to/file.apk}}`

- Android-alkalmazás pusholása egy adott emulátorra/készülékre (felülírja a `$ANDROID_SERIAL`):

`adb -s {{serial_number}} install {{path/to/file.apk}}`

- Újratelepít egy meglévő alkalmazást, megtartva annak adatait:

`adb install -r {{path/to/file.apk}}`

- Egy Android-alkalmazás továbbítása, amely lehetővé teszi a verzió kódjának visszaváltását (csak hibakereső csomagok):

`adb install -d {{path/to/file.apk}}`

- Az alkalmazás manifesztjében felsorolt összes engedély megadása:

`adb install -g {{path/to/file.apk}}`

- Gyorsan frissíthet egy telepített csomagot úgy, hogy csak az APK megváltozott részeit frissíti:

`adb install --fastdeploy {{path/to/file.apk}}`
