# git subtree

> A projektfüggőségek alprojektek formájában történő kezelésének eszköze. További információ: <https://manpages.debian.org/testing/git-man/git-subtree.1.en.html>.

- Git-tárhely hozzáadása alfaként:

`git subtree add --prefix={{path/to/directory/}} --squash {{repository_url}} {{branch_name}}`

- A részfa-tárhely frissítése a legutóbbi commitra:

`git subtree pull --prefix={{path/to/directory/}} {{repository_url}} {{branch_name}}`

- A legutóbbi változtatások beolvasztása a részfa legutóbbi commitjáig a részfába:

`git subtree merge --prefix={{path/to/directory/}} --squash {{repository_url}} {{branch_name}}`

- Commitek átvitele egy részfa tárolóhelyre:

`git subtree push --prefix={{path/to/directory/}} {{repository_url}} {{branch_name}}`

- Új projekttörténet kivonása egy részfa előzményeiből:

`git subtree split --prefix={{path/to/directory/}} {{repository_url}} -b {{branch_name}}`
