# date

> Setze die Systemzeit oder zeige sie an.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/date>.

- Zeige das aktuelle Datum im Format der eingestellten Locale an:

`date +%c`

- Zeige das aktuelle Datum in koordinierter Weltzeit (UTC) im ISO 8601-Format an:

`date -u +%Y-%m-%dT%H:%M:%S%Z`

- Zeige das aktuelle Datum in Unixzeit (vergangene Sekunden seit der Unix-Epoche) an:

`date +%s`

- Konvertiere ein in Unixzeit gegebenes Datum zum Standardformat:

`date -d @{{1473305798}}`

- Konvertiere ein gegebenes Datum zu Unixzeit:

`date -d "{{2018-09-01 00:00}}" +%s --utc`

- Zeige das aktuelle Datum im RFC-3339 Format (`YYYY-MM-DD hh:mm:ss TZ`) an:

`date --rfc-3339=s`

- Setze das aktuelle Datum im Format `MMDDhhmmYYYY.ss` (`YYYY` und `.ss` sind optional):

`date {{093023592021.59}}`

- Zeige die aktuelle ISO-Wochenzahl an:

`date +%V`
