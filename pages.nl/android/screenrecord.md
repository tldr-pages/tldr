# screenrecord

> Neem een video op van een mobiel scherm.
> Opmerking: dit commando kan alleen worden gebruikt via `adb shell`.
> Meer informatie: <https://developer.android.com/tools/adb#screenrecord>.

- Neem het scherm op:

`screenrecord {{pad/naar/bestand}}.mp4`

- Neem het scherm op met een specifieke resolutie:

`screenrecord --size {{1280x720}} {{pad/naar/bestand}}.mp4`

- Neem het scherm op met een specifieke bitrate:

`screenrecord --bit-rate {{6000000}} {{pad/naar/bestand}}.mp4`

- Neem het scherm op met een maximale duur (in seconden, 180 seconden is het maximum):

`screenrecord --time-limit {{180}} {{pad/naar/bestand}}.mp4`

- Toon de help:

`screenrecord --help`
