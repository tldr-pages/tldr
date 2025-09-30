# look

> Wyświetl linie zaczynające się od przedrostka w posortowanym pliku.
> Zobacz także: `grep`, `sort`.
> Więcej informacji: <https://man.freebsd.org/cgi/man.cgi?look>.

- Wyszukaj linie zaczynające się określonym przedrostkiem w określonym pliku:

`look {{przedrostek}} {{ścieżka/do/pliku}}`

- Wyszukuj bez uwzględniania wielkości liter, tylko znaki alfanumeryczne:

`look {{[-f|--ignore-case]}} {{[-d|--alphanum]}} {{przedrostek}} {{ścieżka/do/pliku}}`

- Określ znak kończący ciąg znaków (domyślnie spacja):

`look {{[-t|--terminate]}} {{,}}`

- Wyszukaj w `/usr/share/dict/words` (przyjęte opcje `--ignore-case` i `--alphanum`):

`look {{przedrostek}}`
