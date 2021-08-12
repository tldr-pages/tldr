# git restore

> Restaurați fișierele arborelui de lucru. Necesită versiunea Git 2.23+.
> A se vedea, de asemenea, `git checkout` și `git reset`.
> Mai multe informaţii: <https://git-scm.com/docs/git-restore>

- Restaurați un fișier neetalat la versiunea de comiterea curentă (HEAD):

`git restore {{path/to/file}}`

- Restaurați un fișier neetalat la versiunea unui anumit angajament:

`git restore --source {{commit}} {{path/to/file}}`

- Aruncați toate modificările neetalate la fișierele urmărite:

`git restore :/`

- Unstage un fișier:

`git restore --staged {{path/to/file}}`

- Desenează toate fişierele:

`git restore --staged :/`

- Aruncați toate modificările la fișiere, atât pe etape, cât și pe neetape:

`git restore --worktree --staged :/`

- Selectați interactiv secțiuni de fișiere pentru a restabili:

`git restore --patch`
