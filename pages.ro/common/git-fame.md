# git fame

> Pretty-imprimare contribuții depozit Git.
> Mai multe informaţii: <https://github.com/casperdcl/git-fame>

- Calculați contribuțiile pentru depozitul Git curent:

`git fame`

- Excludeți fișierele/directoarele care se potrivesc cu expresia regulată specificată:

`git fame --excl "{{regular_expression}}"`

- Calculați contribuțiile efectuate după data specificată:

`git fame --since "{{3 weeks ago|2021-05-13}}"`

- Afișarea contribuțiilor în formatul specificat:

`git fame --format {{pipe|yaml|json|csv|tsv}}`

- Afişare contribuţii per extensie fişier:

`git fame --bytype`

- Ignoră modificările spațiului alb:

`git fame --ignore-whitespace`

- Detectați mutările și copiile de linie între fișiere:

`git fame -C`

- Detectați mutările și copiile liniei intra-fișier:

`git fame -M`
