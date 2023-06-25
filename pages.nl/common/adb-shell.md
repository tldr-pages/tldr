# adb shell

> Android Debug Bridge Shell: Voer externe shell-opdrachten uit op een Android-emulatorinstantie of aangesloten Android-apparaten.
> Meer informatie: <https://developer.android.com/studio/command-line/adb>.

- Start een externe interactieve shell op de emulator of het apparaat:

`adb shell`

- Haal alle eigenschappen op van de emulator of het apparaat:

`adb shell getprop`

- Zet alle runtime-machtigingen terug naar hun standaard:

`adb shell pm reset-permissions`

- Een gevaarlijke machtiging voor een toepassing intrekken:

`adb shell pm revoke {{pakket}} {{toestemming}}`

- Activeer een sleutelgebeurtenis:

`adb shell input keyevent {{sleutelcode}}`

- Wis de gegevens van een applicatie op een emulator of apparaat:

`adb shell pm clear {{pakket}}`

- Start een activiteit op emulator of apparaat:

`adb shell am start -n {{pakket}}/{{activiteit}}`

- Start de thuisactiviteit op een emulator of apparaat:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
