# lex

> Generator analizor lexical.
> Având în vedere caietul de sarcini pentru un analizor lexical, generează cod C de punere în aplicare.

- Generarea unui analizor dintr-un fișier Lex:

`lex {{analyser.l}}`

- Specificați fișierul de ieșire:

`lex {{analyser.l}} --outfile {{analyser.c}}`

- Compilarea unui fișier C generat de Lex:

`cc {{path/to/lex.yy.c}} --output {{executable}}`
