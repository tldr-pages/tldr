# git ls-remote

> Comanda Git pentru listarea referințelor într-un depozit la distanță bazat pe nume sau URL.
> Dacă nu sunt date nume sau URL, atunci ramura configurată în amonte va fi utilizată sau origine la distanță dacă prima nu este configurată.
> Mai multe informaţii: <https://git-scm.com/docs/git-ls-remote>

- Afișează toate referințele în depozitul implicit la distanță:

`git ls-remote`

- Afișează doar referințe capete în depozitul implicit la distanță:

`git ls-remote --heads`

- Afișează doar referințe de etichete în depozitul implicit la distanță:

`git ls-remote --tags`

- Afișează toate referințele dintr-un depozit la distanță bazat pe nume sau URL:

`git ls-remote {{repository_url}}`

- Afișați referințele dintr-un depozit la distanță filtrat după un model:

`git ls-remote {{repository_name}} "{{pattern}}"`
