# lex

> Generator voor lexicale analyzers.
> Gegeven de specificatie voor een lexicale analyzer, genereert C-code die deze implementeert.
> Meer informatie: <https://manned.org/lex.1>.

- Genereer een analyzer van een Lex-bestand en sla deze op in het bestand `lex.yy.c`:

`lex {{analyzer.l}}`

- Schrijf de analyzer naar `stdout`:

`lex -{{-stdout|t}} {{analyzer.l}}`

- Specificeer het uitvoerbestand:

`lex {{analyzer.l}} --outfile {{analyzer.c}}`

- Genereer een [B]atch-scanner in plaats van een interactieve scanner:

`lex -B {{analyzer.l}}`

- Compileer een C-bestand dat door Lex is gegenereerd:

`cc {{pad/naar/lex.yy.c}} --output {{uitvoerbaar_bestand}}`
