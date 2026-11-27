# choco new

> Erstelle neue Paket-Beschreibungs-Dateien mit Chocolatey.
> Weitere Informationen: <https://docs.chocolatey.org/en-us/create/commands/new/>.

- Erstelle ein neues Grundgerüst für ein Paket:

`choco new {{paket}}`

- Erstelle ein neues Paket mit einer bestimmten Version:

`choco new {{paket}} --version {{version}}`

- Erstelle ein neues Paket mit einem bestimmten Betreuer*innen-Namen:

`choco new {{paket}} --maintainer {{betreuer*innen_name}}`

- Erstelle ein neues Paket in einem bestimmten Ausgabe-Verzeichnis:

`choco new {{paket}} {{[--out|--output-directory]}} {{pfad/zu/verzeichnis}}`

- Erstelle ein neues Paket mit verschiedenen URLs für die 32-Bit und 64-Bit Installationsroutinen:

`choco new {{paket}} url="{{url}}" url64="{{url}}"`
