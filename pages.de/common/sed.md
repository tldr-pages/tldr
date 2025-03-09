# sed

> Textmanipulation für die Verwendung in Skripten.
> Siehe auch: `awk`, `ed`.
> Mehr Informationen: <https://manpages.debian.org/stable/manpages-de/sed.1.de.html>.

- Ersetze alle Vorkommnisse von `Apfel` (einfache Regex) mit `Mango` (einfache Regex) in allen Eingabezeilen und schreibe das Ergebnis nach `stdout`:

`{{Befehl}} | sed 's/Apfel/Mango/g'`

- Führe ein gegebenes Skript[f]ile und schreibe das Ergebnis nach `stdout`:

`{{Befehl}} | sed -f {{pfad/zu/script.sed}}`

- Schreibe nur die erste Zeile nach `stdout`:

`{{Befehl}} | sed -n '1p'`

- Ersetze alle Vorkommnisse von `Apfel` mit `Mango` in der gegebenen Datei:

`sed --in-place 's/Apfel/Mango/g' {{pfad/zu/datei}}`
