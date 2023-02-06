# flex

> Lexikai elemző generátor. A `lex` alapján. Egy lexikai elemző specifikációja alapján C kódot generál, amely megvalósítja azt. További információ: <https://manned.org/flex>.

- Elemző generálása egy flex fájlból:

`flex {{analyzer.l}}`

- Adja meg a kimeneti fájlt:

`flex --outfile {{analyzer.c}} {{analyzer.l}}`

- Fordítson le egy flex által generált C fájlt:

`cc {{path/to/lex.yy.c}} --output {{executable}}`
