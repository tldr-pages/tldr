# grep

> Findet Ausdrücke in einem Eingabetext.
> Unterstützt einfache Muster und reguläre Ausdrücke.
> Weitere Informationen: <https://www.gnu.org/software/grep/manual/grep.html>.

- Suche nach einem Ausdruck in einer Datei:

`grep "{{ausdruck}}" {{pfad/zu/datei}}`

- Suche nach einem exakten Ausdruck:

`grep --fixed-strings "{{exakter_ausdruck}}" {{pfad/zu/datei}}`

- Benutze erweiterte reguläre Ausdrücke (unterstützt `?`, `+`, `{}`, `()` und `|`) ohne Beachtung der Groß-, Kleinschreibung:

`grep --extended-regexp --ignore-case "{{ausdruck}}" {{pfad/zu/datei}}`

- Zeige 3 Zeilen Kontext um [C], vor [B] oder nach [A] jedem Ergebnis:

`grep --{{context|before-context|after-context}}={{3}} "{{ausdruck}}" {{pfad/zu/datei}}`
