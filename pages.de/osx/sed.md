# sed

> Führe grundlegende Texttransformationen an der Eingabe aus.
> Weitere Informationen: <https://ss64.com/osx/sed.html>.

- Ersetzt das erste Vorkommen einer Zeichenkette in einer Datei und gibt das Ergebnis aus:

`sed 's/{{finde}}/{{ersetze}}/' {{dateiname}}`

- Ersetzt alle Vorkommen eines erweiterten regulären Ausdrucks in einer Datei:

`sed -E 's/{{regulärer_ausdruck}}/{{ersetze}}/g' {{dateiname}}`

- Ersetzt alle Vorkommen einer Zeichenkette [i]n einer Datei, wobei die Datei überschrieben wird (d.h. an Ort und Stelle):

`sed -i '' 's/{{finde}}/{{ersetze}}/g' {{dateiname}}`

- Ersetzt nur die Zeilen, die dem Zeilenmuster entsprechen:

`sed '/{{zeilenmuster}}/s/{{finde}}/{{resetze}}/' {{dateiname}}`

- Druckt nur den Text zwischen der n-ten Zeile bis zur nächsten Leerzeile:

`sed -n '{{zeilennummer}},/^$/p' {{dateiname}}`

- Mehrere Ausdrücke zum Suchen und Ersetzen auf eine Datei anwenden:

`sed -e 's/{{finde}}/{{ersetze}}/' -e 's/{{finde}}/{{ersetze}}/' {{dateiname}}`

- Ersetzt das Trennzeichen `/` durch jedes andere Zeichen, das nicht in den Such- oder Ersetzungsmustern verwendet wird, z. B. `#`:

`sed 's#{{finde}}#{{ersetze}}#' {{dateiname}}`

- Löscht die Zeile an der bestimmten Zeilennummer in einer Datei:

`sed -i '' '{{zeilennummer}}d' {{dateiname}}`
