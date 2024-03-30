# dumpsys

> Stelle Informationen über Android-Systemservices bereit.
> Dieser Befehl kann nur mit `adb shell` verwendet werden.
> Weitere Informationen: <https://developer.android.com/tools/dumpsys>.

- Erhalte diagnostische Informationen über alle Systemservices:

`dumpsys`

- Erhalte diagnostische Informationen über einen bestimmten Systemservice:

`dumpsys {{service}}`

- Liste alle Services, über die `dumpsys` Informationen bereitstellen kann auf:

`dumpsys -l`

- Liste Service-spezifische Argumente für einen Service auf:

`dumpsys {{service}} -h`

- Schließe einen bestimmten Service von den diagnostischen Informationen aus:

`dumpsys --skip {{service}}`

- Gib ein Timeout in Sekunden an (standardmäßig 10s):

`dumpsys -t {{sekunden}}`
