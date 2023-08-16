# adb logcat

> Dump een logboek met systeemberichten.
> Meer informatie: <https://developer.android.com/studio/command-line/logcat>.

- Geef systeemlogboeken weer:

`adb logcat`

- Geef regels weer die overeenkomen met een reguliere expressie:

`adb logcat -e {{reguliere_expressie}}`

- Toon logs voor een tag in een specifieke modus ([V]erbose, [D]ebug, [I]nfo, [W]arning, [E]rror, [F]atal, [S]ilent), andere tags filteren:

`adb logcat {{label}}:{{modus}} *:S`

- Geef logs weer voor React Native-applicaties in [V]erbose mode [S]ilencing andere tags:

`adb logcat ReactNative:V ReactNativeJS:V *:S`

- Toon logboeken voor alle tags met prioriteitsniveau [W]arning en hoger:

`adb logcat *:W`

- Geef logboeken weer voor een specifiek proces:

`adb logcat --pid={{pid}}`

- Logboeken weergeven voor het proces van een specifiek pakket:

`adb logcat --pid=$(adb shell pidof -s {{pakket}})`

- Kleur de log in (gebruik meestal met filters):

`adb logcat -v color`
