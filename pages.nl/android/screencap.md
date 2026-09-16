# screencap

> Maak een screenshot van een mobiel scherm.
> Opmerking: dit commando kan alleen worden gebruikt via `adb shell`.
> Meer informatie: <https://developer.android.com/tools/adb#screencap>.

- Maak een screenshot:

`screencap {{pad/naar/afbeelding.png}}`

- Toon bestandsinhoud naar `stdout` als PNG:

`screencap -p`

- Neem een screenshot en sla deze op via een `adb`-verbinding:

`adb shell screencap -p > {{path/to/afbeelding.png}}`

- Toon de help:

`screencap -h`
