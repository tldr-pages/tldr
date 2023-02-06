# carp

> REPL és build tool a Carp-hoz. További információ: <https://carp-lang.github.io/carp-docs/Manual.html>.

- Indítson el egy REPL-t (interaktív héj):

`carp`

- REPL indítása egyéni prompttal:

`carp --prompt "{{> }}"`

- Építsen egy `carp` fájlt:

`carp -b {{path/to/file.carp}}`

- Egy fájl építése és futtatása:

`carp -x {{path/to/file.carp}}`

- Fájl építése optimalizálás engedélyezésével:

`carp -b --optimize {{path/to/file.carp}}`

- Egy fájl átfordítása C kódba:

`carp --generate-only {{path/to/file.carp}}`
