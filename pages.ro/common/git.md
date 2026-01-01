# git

> Sistem de control al versiunilor distribuit.
> Unele subcomenzi precum `commit`, `add`, `branch`, `switch`, `push`, etc. au propria documentație de utilizare.
> Mai multe informații: <https://git-scm.com/docs/git>.

- Creează un repository Git gol:

`git init`

- Clonează un repository Git la distanță de pe internet:

`git clone {{https://example.com/repo.git}}`

- Vezi starea repository-ului local:

`git status`

- Pregătește toate modificările pentru un commit:

`git add {{[-A|--all]}}`

- Confirmați modificările în istoricul versiunilor:

`git commit {{[-m|--message]}} {{text_mesaj}}`

- Trimite commit-urile locale către un repository la distanță:

`git push`

- Trage orice modificare făcută la distanță:

`git pull`

- Resetează totul așa cum era în ultimul commit:

`git reset --hard; git clean {{[-f|--force]}}`
