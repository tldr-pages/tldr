# gops

> Instrumentul CLI care listează și diagnostichează Du-te procesele care rulează în prezent pe sistemul tău.
> Mai multe informaţii: <https://github.com/google/gops>

- Imprimați toate procesele du-te care rulează la nivel local:

`gops`

- Imprimați mai multe informații despre un proces:

`gops {{pid}}`

- Afișează un arbore de proces:

`gops tree`

- Imprimați trasarea stivei curente dintr-un program țintă:

`gops stack {{pid|addr}}`

- Imprimați statisticile curente ale memoriei runtime:

`gops memstats {{pid|addr}}`
