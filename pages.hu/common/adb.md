# adb

> Android Debug Bridge: kommunikáció egy Android emulátor példányával vagy csatlakoztatott Android eszközökkel. Néhány alparancsnak, mint például a `adb shell`, saját használati dokumentációja van. További információ: <https://developer.android.com/studio/command-line/adb>.

- Ellenőrizze, hogy az adb szerverfolyamat fut-e, és indítsa el:

`adb start-server`

- Az adb szerverfolyamat befejezése:

`adb kill-server`

- Távoli héj indítása a cél emulátor/készülék példányban:

`adb shell`

- Android-alkalmazás tolása az emulátorba/készülékre:

`adb install -r {{path/to/file.apk}}`

- Fájl/könyvtár másolása a céleszközről:

`adb pull {{path/to/device_file_or_directory}} {{path/to/local_destination_directory}}`

- Fájl/könyvtár másolása a céleszközre:

`adb push {{path/to/local_file_or_directory}} {{path/to/device_destination_directory}}`

- A csatlakoztatott eszközök listájának lekérdezése:

`adb devices`
