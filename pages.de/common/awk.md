# awk

> Eine vielseitige Programmiersprache zum Arbeiten mit Dateien.
> Hinweis: Verschiedene AWK-Implementierungen machen dies oft zu einem Symlink auf ihre Binärdatei.
> Siehe auch: `gawk`.
> Weitere Informationen: <https://github.com/onetrueawk/awk>.

- Gib die fünfte Spalte (auch Feld genannt) in einer durch Leerzeichen getrennten Datei aus:

`awk '{print $5}' {{pfad/zu/datei}}`

- Gib die zweite Spalte der Zeilen aus, die "foo" enthalten, in einer durch Leerzeichen getrennten Datei:

`awk '/{{foo}}/ {print $2}' {{pfad/zu/datei}}`

- Gib die letzte Spalte jeder Zeile in einer Datei aus, verwende ein Komma (statt Leerzeichen) als Feldtrennzeichen:

`awk -F ',' '{print $NF}' {{pfad/zu/datei}}`

- Summiere die Werte in der ersten Spalte einer Datei und gib die Gesamtsumme aus:

`awk '{s+=$1} END {print s}' {{pfad/zu/datei}}`

- Gib jede dritte Zeile beginnend bei der ersten Zeile aus:

`awk 'NR%3==1' {{pfad/zu/datei}}`

- Gib verschiedene Werte basierend auf Bedingungen aus:

`awk '{if ($1 == "foo") print "Exakte Übereinstimmung foo"; else if ($1 ~ "bar") print "Teilweise Übereinstimmung bar"; else print "Baz"}' {{pfad/zu/datei}}`

- Gib alle Zeilen aus, deren Wert in der zehnten Spalte zwischen einem Minimum und einem Maximum liegt:

`awk '($10 >= {{min_wert}} && $10 <= {{max_wert}})' {{pfad/zu/datei}}`

- Gib eine Tabelle von Benutzern mit UID >=1000 mit Kopfzeile und formatierter Ausgabe aus, verwende Doppelpunkt als Trennzeichen (`%-20s` bedeutet: 20 linksbündige Zeichen, `%6s` bedeutet: 6 rechtsbündige Zeichen):

`awk 'BEGIN {FS=":";printf "%-20s %6s %25s\n", "Name", "UID", "Shell"} $4 >= 1000 {printf "%-20s %6d %25s\n", $1, $4, $7}' /etc/passwd`
