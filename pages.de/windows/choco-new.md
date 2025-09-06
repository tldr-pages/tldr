# choco new

> Erstelle neue Paket-Beschreibungs-Dateien mit Chocolatey.
> Weitere Informationen: <https://chocolatey.org/docs/commands-new>.

- Erstelle ein neues Grundgerüst für ein Paket:

`choco new {{paket_name}}`

- Erstelle ein neues Paket mit einer bestimmten Version:

`choco new {{paket_name}} --version {{version}}`

- Erstelle ein neues Paket mit einem bestimmten Betreuer*innen-Namen:

`choco new {{paket_name}} --maintainer {{betreuer*innen_name}}`

- Erstelle ein neues Paket in einem bestimmten Ausgabe-Verzeichnis:

`choco new {{paket_name}} --output-directory {{pfad/zu/verzeichnis}}`

- Erstelle ein neues Paket mit verschiedenen URLs für die 32-Bit und 64-Bit Installationsroutinen:

`choco new {{paket_name}} url="{{url}}" url64="{{url}}"`
