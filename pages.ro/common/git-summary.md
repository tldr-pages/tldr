# git summary

> Afișați informații despre un depozit Git.
> Parte din `git-extras`.
> Mai multe informaţii: <https://github.com/tj/git-extras/blob/master/Commands.md#git-summary>

- Afișează date despre un depozit Git:

`git summary`

- Afișarea datelor despre un depozit Git, deoarece o comisie-ish:

`git summary {{commit|branch_name|tag_name}}`

- Afișarea datelor despre un depozit Git, îmbinarea angajatorilor folosind diferite e-mailuri în 1 statistică pentru fiecare autor:

`git summary --dedup-by-email`

- Afișează date despre un depozit Git, indicând numărul de linii modificate de fiecare contribuitor:

`git summary --line`
