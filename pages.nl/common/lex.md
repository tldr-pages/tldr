# lex

> Generator voor lexicale analyzers.
> Gegeven de specificatie voor een lexicale analyzer, genereert C-code die deze implementeert.
> Opmerking: op de meeste grote besturingssystemen is dit commando een alias voor `flex`.
> Meer informatie: <https://manned.org/lex>.

- Genereer een analyzer van een Lex-bestand en sla deze op in het bestand `lex.yy.c`:

`lex {{analyzer.l}}`

- Specificeer het uitvoerbestand:

`lex -t {{analyzer.l}} > {{analyzer.c}}`

- Compileer een C-bestand dat door Lex is gegenereerd:

`c99 {{pad/naar/lex.yy.c}} -o {{uitvoerbaar_bestand}}`
