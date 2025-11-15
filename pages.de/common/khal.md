# khal

> Eine textbasierte Kalender- und Planungsanwendung für die Kommandozeile.
> Weitere Informationen: <https://lostpackets.de/khal>.

- Starte khal im interaktiven Modus:

`ikhal`

- Gib alle Termine aus, die im Kalender "privat" in den nächsten sieben Tagen geplant sind:

`khal list -a {{privat}} {{today}} {{7d}}`

- Gib alle Termine aus, die in Kalendern außer "privat" für morgen um 10 Uhr geplant sind:

`khal at -d {{privat}} {{tomorrow}} {{10:00}}`

- Gib einen Kalender mit einer Liste an Terminen für die nächsten drei Monate aus:

`khal calendar`

- Füge dem Kalender "privat" einen neuen Termin hinzu:

`khal new -a {{privat}} {{2020-09-08}} {{18:00}} {{18:30}} "{{Zahnarzttermin}}"`
