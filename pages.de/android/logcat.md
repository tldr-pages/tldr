# logcat

> Gib ein Protokoll aller System-Logs aus.
> Weitere Informationen: <https://developer.android.com/tools/logcat>.

- Gib ein Protokoll aller System-Logs aus:

`logcat`

- Schreibe alle System-Logs in eine Datei:

`logcat -f {{pfad/zu/datei}}`

- Gib Zeilen aus, die einem regulären Ausdruck entsprechen:

`logcat --regex {{regex}}`

- Gib System-Logs für die spezifizierte PID aus:

`logcat --pid {{pid}}`

- Gib System-Logs für den Prozess eines bestimmten Packets aus:

`logcat --pid $(pidof -s {{packet}})`
