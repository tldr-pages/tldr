# cut

> Schneide Felder von stdin oder einer Datei aus.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/cut>.

- Schneide die ersten 16 Zeichen jeder Zeile von stdin aus:

`cut -c {{1-16}}`

- Schneide die ersten 16 Zeichen jeder Zeile der angegebenen Datei aus:

`cut -c {{1-16}} {{pfad/zu/datei}}`

- Schneide alles ab dem dritten Zeichen bis zum Ende der Zeile aus:

`cut -c {{3-}}`

- Schneide das fünfte Feld jeder Zeile aus und nutze den Doppelpunkt als Trennzeichen (standardmäßig Tab):

`cut -d'{{:}}' -f{{5}}`

- Schneide das 2. und 10. Feld jeder Zeile aus und nutze Semikolon als Trennzeichen:

`cut -d'{{;}}' -f{{2,10}}`

- Schneide alles ab dem dritten Zeichen bis zum Ende der Zeile aus und nutze Leerzeichen als Trennzeichen:

`cut -d'{{ }}' -f{{3-}}`
