# po4a-gettextize

> Egy fájl PO-fájllá történő átalakítása. További információ: <https://po4a.org/man/man1/po4a-gettextize.1.php>.

- Szöveges fájl átalakítása PO-fájllá:

`po4a-gettextize --format {{text}} --master {{path/to/master.txt}} --po {{path/to/result.po}}`

- A rendelkezésre álló formátumok listájának lekérdezése:

`po4a-gettextize --help-format`

- Konvertáljon egy szöveges fájlt egy lefordított dokumentummal együtt PO-fájlba (`-l` opció többször is megadható):

`po4a-gettextize --format {{text}} --master {{path/to/master.txt}} --localized {{path/to/translated.txt}} --po {{path/to/result.po}}`
