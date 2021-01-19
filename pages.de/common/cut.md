# cut

> Entferne Felder von stdin oder einer Datei.

- Entferne die ersten 16 Zeichen jeder Zeile von stdin:

`cut -c {{1-16}}`

- Entferne die ersten 16 Zeichen jeder Zeile der angegebenen Datei:

`cut -c {{1-16}} {{datei}}`

- Entferne alles ab dem dritten Zeichen bis zum Ende der Zeile:

`cut -c {{3-}}`

- Entferne das fünfte Feld jeder Zeile, nutze Doppelpunkt als Trennzeichen (Standart ist Tab):

`cut -d'{{:}}' -f{{5}}`

- Entferne das 2. und 10. Feld jeder Zeile, nutze Semikolon als Trennzeichen:

`cut -d'{{;}}' -f{{2,10}}`

- Entferne alles ab dem dritten Zeichen bis zum Ende der Zeile, nutze Leerzeichen als Trennzeichen:

`cut -d'{{ }}' -f{{3-}}`
