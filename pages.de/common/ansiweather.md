# ansiweather

> Ein Shell-Skript um die aktuellen Wetterbedingungen in einem Terminal anzuzeigen.
> Weitere Informationen: <https://github.com/fcambus/ansiweather>.

- Zeigt eine Vorhersage für die nächsten fünf Tage für Rzeszow, Polen in metrischen Einheiten an:

`ansiweather -u {{metric}} -f {{5}} -l {{Rzeszow,PL}}`

- Zeigt eine Vorhersage mit Symbolen und Tageslichtdaten für den aktuellen Standort an:

`ansiweather -s {{true}} -d {{true}}`

- Zeigt eine Vorhersage mit Wind- und Luftfeuchtigkeitsdaten für den aktuellen Standort an:

`ansiweather -w {{true}} -h {{true}}`
