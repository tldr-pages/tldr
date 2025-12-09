# adb

> Android Debug-Brug: communiceer met een Android-emulator of een aangesloten Android-apparaat.
> Sommige subcommando's zoals `shell` hebben hun eigen documentatie.
> Meer informatie: <https://developer.android.com/tools/adb>.

- Controleer of het adb serverproces draait en start het:

`adb start-server`

- Sluit het adb serverproces:

`adb kill-server`

- Start een remote shell voor de doel-emulator of apparaat-instantie:

`adb shell`

- Stuur een Android-applicatie naar de emulator/het apparaat:

`adb install -r {{pad/naar/bestand.apk}}`

- Kopiëer een bestand/map van het doelapparaat:

`adb pull {{pad/naar/extern/bestand_of_map}} {{pad/naar/lokaal/bestand_of_map}}`

- Kopiëer een bestand/map naar het doelapparaat:

`adb push {{pad/naar/lokaal/bestand_of_map}} {{pad/naar/extern/bestand_of_map}}`

- Toon alle aangesloten apparaten:

`adb devices`

- Specificeer naar welk apparaat de opdrachten verzonden dienen te worden als er meerdere apparaten zijn:

`adb -s {{apparaat_ID}} {{shell}}`
