# tr

> Übersetze Zeichen: Führe Ersetzungen basierend auf einzelnen Zeichen und Zeichensätzen durch.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/manual/html_node/tr-invocation.html>.

- Ersetze alle Vorkommen eines Zeichens in einer Datei und gib das Ergebnis aus:

`tr < {{pfad/zu/datei}} {{zu_findendes_zeichen}} {{ersatzzeichen}}`

- Ersetze alle Vorkommen eines Zeichens aus der Ausgabe eines anderen Befehls:

`echo {{text}} | tr {{zu_findendes_zeichen}} {{ersatzzeichen}}`

- Ordne jedes Zeichen des ersten Satzes dem entsprechenden Zeichen des zweiten Satzes zu:

`tr < {{pfad/zu/datei}} '{{abcd}}' '{{jkmn}}'`

- Lösche alle Vorkommen des angegebenen Zeichensatzes aus der Eingabe:

`tr < {{pfad/zu/datei}} {{[-d|--delete]}} '{{eingabezeichen}}'`

- Komprimiere eine Reihe identischer Zeichen zu einem einzelnen Zeichen:

`tr < {{pfad/zu/datei}} {{[-s|--squeeze-repeats]}} '{{eingabezeichen}}'`

- Übersetze den Inhalt einer Datei in Großbuchstaben:

`tr < {{pfad/zu/datei}} "[:lower:]" "[:upper:]"`

- Entferne nicht druckbare Zeichen aus einer Datei:

`tr < {{pfad/zu/datei}} {{[-cd|--complement --delete]}} "[:print:]"`
