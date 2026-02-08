# uniq

> Gib die eindeutigen Zeilen einer Eingabe oder Datei aus.
> Da es keine wiederholten Zeilen erkennt, es sei denn, sie sind nebeneinander, müssen wir sie zuerst sortieren.
> Siehe auch: `sort`.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/manual/html_node/uniq-invocation.html>.

- Gib jede Zeile einmal aus:

`sort {{pfad/zu/datei}} | uniq`

- Gib nur eindeutige Zeilen aus:

`sort {{pfad/zu/datei}} | uniq {{[-u|--unique]}}`

- Gib nur doppelte Zeilen aus:

`sort {{pfad/zu/datei}} | uniq {{[-d|--repeated]}}`

- Gib die Anzahl der Vorkommen jeder Zeile zusammen mit der Zeile aus:

`sort {{pfad/zu/datei}} | uniq {{[-c|--count]}}`

- Gib die Anzahl der Vorkommen jeder Zeile aus, sortiert nach der häufigsten:

`sort {{pfad/zu/datei}} | uniq {{[-c|--count]}} | sort {{[-nr|--numeric-sort --reverse]}}`

- Vergleiche nur die ersten 10 Zeichen jeder Zeile auf Eindeutigkeit:

`sort {{pfad/zu/datei}} | uniq {{[-w|--check-chars]}} 10`

- Vergleiche den Text nach den ersten 5 Zeichen jeder Zeile auf Eindeutigkeit:

`sort {{pfad/zu/datei}} | uniq {{[-s|--skip-chars]}} 5`
