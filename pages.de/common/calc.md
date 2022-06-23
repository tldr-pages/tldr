# calc

> Ein interaktiver Rechner im Terminal mit beliebiger Genauigkeit.
> Weitere Informationen: <https://github.com/lcn2/calc>.

- Starte `calc` im interaktiven Modus:

`calc`

- Führe eine nicht-interaktive Berechnung durch:

`calc '{{85 * (36 / 4)}}'`

- Führe eine Berechnung durch ohne die Ausgabe zu formatieren (für das Benutzen mit Pipes):

`calc -p '{{4/3 * pi() * 5^3}}'`

- Führe eine Berechnung durch und wechsle dann in den interaktiven Modus:

`calc -i '{{sqrt(2)}}'`

- Starte `calc` in einem bestimmten Berechtigungs-Modus (0 bis 7, standardmäßig 7):

`calc -m {{mode}}`

- Öffne die Bedienungsanleitung von `calc`:

`calc help`

- Öffne eine Einführung zu `calc`:

`calc help intro`

- Öffne eine Übersicht von `calc`:

`calc help overview`
