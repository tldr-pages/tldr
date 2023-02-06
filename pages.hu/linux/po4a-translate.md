# po4a-translate

> Egy PO fájl visszaváltása dokumentációs formátumba. A megadott PO fájlnak a `po4a-gettextize` által készített POT fájl fordításának kell lennie. További információ: <https://po4a.org/man/man1/po4a-translate.1.php>.

- Egy lefordított PO-fájl visszaalakítása dokumentummá:

`po4a-translate --format {{text}} --master {{path/to/master.doc}} --po {{path/to/result.po}} --localized {{path/to/translated.txt}}`

- A rendelkezésre álló formátumok listájának lekérdezése:

`po4a-translate --help-format`
