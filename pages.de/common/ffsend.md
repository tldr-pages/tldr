# ffsend

> Teile Dateien einfach und sicher in der Command-line.
> Weitere Informationen: <https://gitlab.com/timvisee/ffsend>.

- Lade eine Datei hoch:

`ffsend upload {{pfad/zu/datei}}`

- Lade eine Datei herunter:

`ffsend download {{url}}`

- Lade eine Datei mit Passwort hoch:

`ffsend upload {{pfad/zu/datei}} {{[-p|--password]}} {{passwort}}`

- Lade eine passwortgeschützte Datei herunter:

`ffsend download {{url}} {{[-p|--password]}} {{passwort}}`

- Lade eine Datei hoch und erlaube maximal 4 Downloads:

`ffsend upload {{pfad/zu/datei}} {{[-d|--downloads]}} {{4}}`
