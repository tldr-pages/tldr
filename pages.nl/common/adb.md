# adb

> Android Debug-Brug: communiceer met een Android-emulator of een aangesloten Android-apparaat.
> Sommige subcommando's zoals `adb shell` hebben hun eigen documentatie.
> Meer informatie: <https://developer.android.com/studio/command-line/adb>.

- Controleer of het adb serverproces draait en start het:

`adb start-server`

- Sluit het adb serverproces:

`adb kill-server`

- Start een afstandshell voor de doelemulator of apparaatinstantie:

`adb shell`

- Stuur een Android-applicatie naar de emulator/het apparaat:

`adb install -r {{pad/naar/bestand.apk}}`

- Kopiëer een bestand/map van het doelapparaat:

`adb pull {{pad/naar/extern/bestand_of_map}} {{pad/naar/lokaal/bestand_of_map}}`

- Kopiëer een bestand/map naar het doelapparaat:

`adb push {{pad/naar/lokaal/bestand_of_map}} {{pad/naar/extern/bestand_of_map}}`

- Krijg een lijst met aangesloten apparaten:

`adb devices`
