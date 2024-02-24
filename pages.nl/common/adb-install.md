# adb install

> Android Debug Bridge-installatie: push pakketten naar een Android-emulatorinstantie of aangesloten Android-apparaten.
> Meer informatie: <https://developer.android.com/tools/adb>.

- Push een Android-applicatie naar een emulator/apparaat:

`adb install {{pad/naar/bestand.apk}}`

- Een Android-applicatie naar een specifieke emulator/apparaat pushen (heeft voorrang op `$ANDROID_SERIAL`):

`adb -s {{serienummer}} install {{pad/naar/bestand.apk}}`

- Installeer een bestaande app opnieuw, waarbij de gegevens behouden blijven:

`adb install -r {{pad/naar/bestand.apk}}`

- Een Android-applicatie pushen die downgrade van versiecode mogelijk maakt (alleen foutopsporingspakketten):

`adb install -d {{pad/naar/bestand.apk}}`

- Verleen alle machtigingen die worden vermeld in het app-manifest:

`adb install -g {{pad/naar/bestand.apk}}`

- Werk snel een geïnstalleerd pakket bij door alleen de delen van de APK bij te werken die zijn gewijzigd:

`adb install --fastdeploy {{pad/naar/bestand.apk}}`
