# flex

> Lexicale analysator generator.
> Gegeven de specificatie voor een lexicale analysator, genereert C-code die het implementeert.
> Meer informatie: <https://manned.org/flex>.

- Genereer een analyzer uit een Lex-bestand en sla het op in het bestand `lex.yy.c`:

`flex {{analyzer.l}}`

- Analysator naar `stdout` schrijven:

`flex {{[-t|--stdout]}} {{analyzer.l}}`

- Geef het uitvoerbestand op:

`flex {{analyzer.l}} {{[-o|--outfile]}} {{analyzer.c}}`

- Genereer een batch scanner in plaats van een interactieve scanner:

`flex {{[-B|--batch]}} {{analyzer.l}}`

- Compileer een C-bestand gegenereerd door Lex:

`cc {{pad/naar/lex.yy.c}} -o {{executable}}`
