# adb reverse

> Keer socketverbindingen om van een verbonden Android-apparaat of -emulator.
> Meer informatie: <https://developer.android.com/tools/adb>.

- Toon alle omgekeerde socketverbindingen van emulators en apparaten:

`adb reverse --list`

- Keer een TCP-poort om van de enige verbonden emulator of apparaat naar localhost:

`adb reverse tcp:{{externe_poort}} tcp:{{lokale_poort}}`

- Keer een TCP-poort om van een specifieke emulator of apparaat (via apparaat-ID of [s]erienummer) naar localhost:

`adb -s {{apparaat_ID}} adb reverse tcp:{{externe_poort}} tcp:{{lokale_poort}}`

- Verwijder omgekeerde socketverbindingen van een emulator of apparaat:

`adb reverse --remove tcp:{{externe_poort}}`

- Verwijder alle omgekeerde socketverbindingen van alle emulators en apparaten:

`adb reverse --remove-all`
