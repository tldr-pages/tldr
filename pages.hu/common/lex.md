# lex

> Lexikai elemző generátor. Egy lexikai elemző specifikációja alapján C kódot generál, amely megvalósítja azt. További információ: <https://manned.org/lex.1>.

- Elemző generálása egy Lex fájlból:

`lex {{analyzer.l}}`

- Adja meg a kimeneti fájlt:

`lex {{analyzer.l}} --outfile {{analyzer.c}}`

- A Lex által generált C fájl lefordítása:

`cc {{path/to/lex.yy.c}} --output {{executable}}`
