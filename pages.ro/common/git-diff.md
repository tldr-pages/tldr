# git diff

> Afișează modificările fișierelor urmărite.
> Mai multe informaţii: <https://git-scm.com/docs/git-diff>

- Arată modificările neorganizate, necomise:

`git diff`

- Afișează toate modificările necomise (inclusiv cele pe etape):

`git diff HEAD`

- Afișează numai modificările în etape (adăugate, dar nu încă angajate):

`git diff --staged`

- Arată modificările din toate angajările de la o dată/oră dată (o expresie a datei, de exemplu „1 săptămână 2 zile” sau o dată ISO):

`git diff 'HEAD@{3 months|weeks|days|hours|seconds ago}'`

- Afișează numai numele fișierelor modificate de la o anumită comitere:

`git diff --name-only {{commit}}`

- Ieșiți un rezumat al creațiilor de fișiere, redenumirile și modificările de mod de la un anumit angajament:

`git diff --summary {{commit}}`

- Comparați un singur fișier între două ramuri sau angajamente:

`git diff {{branch_1}}..{{branch_2}} [--] {{path/to/file}}`

- Comparați fișiere diferite de la ramura curentă la altă ramură:

`git diff {{branch}}:{{path/to/file2}} {{path/to/file}}`
