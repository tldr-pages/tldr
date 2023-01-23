# log

> Naplózási rendszerek megtekintése, exportálása és konfigurálása. További információ: <https://www.dssw.co.uk/reference/log.html>.

- Élő rendszernaplók streamelése:

`log stream`

- A `syslog` címre küldött naplófájlok streamelése egy adott PID azonosítóval rendelkező folyamatból:

`log stream --process {{process_id}}`

- Egy adott nevű folyamatból a syslogba küldött naplók megjelenítése:

`log show --predicate "process == '{{process_name}}'"`

- Az elmúlt egy óra összes naplójának exportálása lemezre:

`sudo log collect --last {{1h}} --output {{path/to/file.logarchive}}`
