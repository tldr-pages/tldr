# git range-diff

> Comparați două intervale de comitere (de exemplu, două versiuni ale unei sucursale).
> Mai multe informaţii: <https://git-scm.com/docs/git-range-diff>

- Diff modificările a două angajări individuale:

`git range-diff {{commit_1}}^! {{commit_2}}^!`

- Difff schimbările noastre și ale lor de strămoșul lor comun, de exemplu, după o relasare interactivă:

`git range-diff {{theirs}}...{{ours}}`

- Diff modificările a două intervale de angajament, de exemplu pentru a verifica dacă conflictele au fost rezolvate în mod corespunzător atunci când rebasing se angajează de la `base1` la `base2`:

`git range-diff {{base1}}..{{rev1}} {{base2}}..{{rev2}}`
