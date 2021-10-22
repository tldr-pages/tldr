# grep

> Findet Ausdrücke in einem Eingabetext.
> Unterstützt einfache Muster und reguläre Ausdrücke.
> Weitere Informationen: <https://www.gnu.org/software/grep/manual/grep.html>.

- Suche nach einem Ausdruck in einer Datei:

`grep {{ausdruck}} {{pfad/zu/datei}}`

- Suche nach einem exakten Ausdruck:

`grep -F {{exakter_ausdruck}} {{pfad/zu/datei}}`

- Suche nach Ausdrücken [R]ekursiv im aktuellen Verzeichnis, zeige zugehörige Zeilen[n]ummern und [I]gnoriere Binärdateien:

`grep -RIn {{ausdruck}} .`

- Benutze erweiterte reguläre Ausdrücke (unterstützt `?`, `+`, `{}`, `()` und `|`) ohne Beachtung der Groß-, Kleinschreibung:

`grep -Ei {{ausdruck}} {{pfad/zu/datei}}`

- Zeige 3 Zeilen Kontext um [C], vor [B] oder nach [A] jedem Ergebnis:

`grep -{{C|B|A}} 3 {{ausdruck}} {{pfad/zu/datei}}`

- Gib den Dateinamen mit zugehöriger Zeilennummer für jedes Ergebnis aus:

`grep -Hn {{ausdruck}} {{pfad/zu/datei}}`

- Benutze STDIN, anstatt einer Datei:

`echo "input" | grep {{ausdruck}}`

- In[v]ertiere das Ergebnis um bestimmte Ausdrücke auszuschließen:

`grep -v {{ausdruck}}`
