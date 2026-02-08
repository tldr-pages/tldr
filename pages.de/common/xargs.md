# xargs

> Führe einen Befehl mit gepipten Argumenten aus, die von einem anderen Befehl, einer Datei etc. stammen.
> Die Eingabe wird als ein einziger Textblock behandelt und anhand von Leerzeichen, Tabs, Zeilenumbrüchen und Dateiende in separate Teile aufgeteilt.
> Siehe auch: `parallel`.
> Weitere Informationen: <https://www.gnu.org/software/findutils/manual/html_mono/find.html#Invoking-xargs>.

- Führe einen Befehl aus, wobei die Eingabedaten als Argumente verwendet werden:

`{{argumenten_quelle}} | xargs {{befehl}}`

- Führe mehrere verkettete Befehle auf den Eingabedaten aus:

`{{argumenten_quelle}} | xargs sh -c "{{befehl1}} && {{befehl2}} | {{befehl3}}"`

- Gzip alle Dateien mit der Erweiterung `.log` und nutze dabei mehrere Threads (`-print0` verwendet ein Nullzeichen zum Aufteilen von Dateinamen und `--null` verwendet es als Trennzeichen):

`find . -name '*.log' -print0 | xargs {{[-0|--null]}} {{[-P|--max-procs]}} {{4}} {{[-n|--max-args]}} 1 gzip`

- Führe den Befehl einmal pro Argument aus:

`{{argumenten_quelle}} | xargs {{[-n|--max-args]}} 1 {{befehl}}`

- Führe den Befehl einmal für jede Eingabezeile aus, wobei alle Vorkommen des Platzhalters (hier als `_` markiert) durch die Eingabezeile ersetzt werden:

`{{argumenten_quelle}} | xargs -I _ {{befehl}} _ {{optionale_extra_argumente}}`

- Parallel ausgeführte Ausführungen von bis zu `max-procs` Prozessen gleichzeitig; der Standard ist 1. Wenn `max-procs` 0 ist, führt xargs so viele Prozesse aus wie möglich:

`{{argumenten_quelle}} | xargs {{[-P|--max-procs]}} {{max_procs}} {{befehl}}`

- Frage den Benutzer vor der Ausführung des Befehls nach Bestätigung (bestätige mit `y` oder `Y`):

`{{argumenten_quelle}} | xargs {{[-p|--interactive]}} {{befehl}}`

- Erlaube dem Befehl den Zugriff auf das Terminal für interaktive Eingabe:

`{{argumenten_quelle}} | xargs {{[-o|--open-tty]}} {{befehl}}`
