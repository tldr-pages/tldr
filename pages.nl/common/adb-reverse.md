# adb reverse

> Android Debug Bridge Reverse: omgekeerde socketverbindingen van een Android-emulatorinstantie of verbonden Android-apparaten.
> Meer informatie: <https://developer.android.com/tools/adb>.

- Maak een lijst van alle omgekeerde socketverbindingen van emulators en apparaten:

`adb reverse --list`

- Keer een TCP-poort om van een emulator of apparaat naar localhost:

`adb reverse tcp:{{externe_poort}} tcp:{{lokale_poort}}`

- Verwijder omgekeerde socketverbindingen van een emulator of apparaat:

`adb reverse --remove tcp:{{externe_poort}}`

- Verwijder alle omgekeerde socketverbindingen van alle emulators en apparaten:

`adb reverse --remove-all`
