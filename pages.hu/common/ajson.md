# ajson

> JSONPath JSON objektumokon történő végrehajtása. További információ: <https://github.com/spyzhov/ajson>.

- JSON olvasása egy fájlból és egy megadott JSONPath kifejezés végrehajtása:

`ajson '{{$..json[?(@.path)]}}' {{path/to/file.json}}`

- JSON beolvasása a `stdin` oldalról és egy megadott JSONPath kifejezés végrehajtása:

`cat {{path/to/file.json}} | ajson '{{$..json[?(@.path)]}}'`

- JSON beolvasása egy URL-címről és egy megadott JSONPath-kifejezés kiértékelése:

`ajson '{{avg($..price)}}' '{{https://example.com/api/}}'`

- Egyszerű JSON beolvasása és egy érték kiszámítása:

`echo '{{3}}' | ajson '{{2 * pi * $}}'`
