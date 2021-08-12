# flex

> Generator analizor lexical. Bazat pe `lex`.
> Având în vedere caietul de sarcini pentru un analizor lexical, generează cod C de punere în aplicare.
> Mai multe informaţii: <https://manned.org/flex>

- Generarea unui analizor dintr-un fișier flex:

`flex {{analyser.l}}`

- Specificați fișierul de ieșire:

`flex --outfile {{analyser.c}} {{analyser.l}}`

- Compilați un fișier C generat de flex:

`cc {{path/to/lex.yy.c}} --output {{executable}}`
