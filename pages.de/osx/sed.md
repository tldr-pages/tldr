# sed

> Führe grundlegende Texttransformationen an der Eingabe aus.
> Weitere Informationen: <https://ss64.com/osx/sed.html>.

- Ersetze das erste Vorkommen einer Zeichenkette in einer Datei und gibt das Ergebnis aus:

`sed 's/{{finde}}/{{ersetze}}/' {{Pfad/zu/Datei}}`

- Ersetze alle Vorkommen eines erweiterten regulären Ausdrucks in einer Datei:

`sed -E 's/{{regulärer_ausdruck}}/{{ersetze}}/g' {{Pfad/zu/Datei}}`

- Ersetze alle Vorkommen einer Zeichenkette [i]n einer Datei, wobei die Datei überschrieben wird (d.h. an Ort und Stelle):

`sed -i '' 's/{{finde}}/{{ersetze}}/g' {{Pfad/zu/Datei}}`

- Ersetze nur die Zeilen, die dem Zeilenmuster entsprechen:

`sed '/{{zeilenmuster}}/s/{{finde}}/{{resetze}}/' {{Pfad/zu/Datei}}`

- Druck nur den Text zwischen der n-ten Zeile bis zur nächsten Leerzeile:

`sed -n '{{zeilennummer}},/^$/p' {{Pfad/zu/Datei}}`

- Suche und Ersetzen mehrere Ausdrücke in einer Datei:

`sed -e 's/{{finde}}/{{ersetze}}/' -e 's/{{finde}}/{{ersetze}}/' {{Pfad/zu/Datei}}`

- Ersetze das Trennzeichen `/` durch jedes andere Zeichen, das nicht in den Such- oder Ersetzungsmustern verwendet wird, z. B. `#`:

`sed 's#{{finde}}#{{ersetze}}#' {{Pfad/zu/Datei}}`

- Lösche die Zeile an der bestimmten Zeilennummer in einer Datei:

`sed -i '' '{{zeilennummer}}d' {{Pfad/zu/Datei}}`
