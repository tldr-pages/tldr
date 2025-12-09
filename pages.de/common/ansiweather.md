# ansiweather

> Ein Shell-Skript um die aktuellen Wetterbedingungen in einem Terminal anzuzeigen.
> Weitere Informationen: <https://github.com/fcambus/ansiweather>.

- Zeige eine Vorhersage für die nächsten sieben Tage für Rzeszow, Polen in metrischen Einheiten an:

`ansiweather -u metric -f 7 -l {{Rzeszow,PL}}`

- Zeige eine Vorhersage mit Symbolen und Tageslichtdaten für den aktuellen Standort an:

`ansiweather -F -s true -d true`

- Zeige eine Vorhersage mit Wind- und Luftfeuchtigkeitsdaten für den aktuellen Standort an:

`ansiweather -w true -h true`
