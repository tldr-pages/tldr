# duf

> Festplattennutzung/freie Verwendbarkeit.
> Siehe auch: `ncdu`, `df`.
> Weitere Informationen: <https://github.com/muesli/duf#usage>.

- Liste zugängliche Geräte auf:

`duf`

- Liste alles auf (auch pseudo-, doppelte oder unzugängliche Dateisysteme):

`duf --all`

- Zeige nur konkrete Geräte oder Mountpoints:

`duf {{pfad/zu/verzeichnis1 pfad/zu/verzeichnis2 ...}}`

- Sortiere die Ergebnisse nach einem spezifischen Kriterium:

`duf --sort {{size|used|avail|usage}}`
