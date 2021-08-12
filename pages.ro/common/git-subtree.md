# git subtree

> Instrument pentru gestionarea dependențelor de proiect ca subproiecte.
> Mai multe informaţii: <https://manpages.debian.org/testing/git-man/git-subtree.1.en.html>

- Adăugați un depozit Git ca subarbore:

`git subtree add --prefix={{path/to/directory/}} --squash {{repository_url}} {{branch_name}}`

- Actualizați depozitul de subarbore la cel mai recent angajament:

`git subtree pull --prefix={{path/to/directory/}} {{repository_url}} {{branch_name}}`

- Îmbinați modificările recente până la cel mai recent subarbore se angajează în subarbore:

`git subtree merge --prefix={{path/to/directory/}} --squash {{repository_url}} {{branch_name}}`

- Push se angajează la un depozit de subarbore:

`git subtree push --prefix={{path/to/directory/}} {{repository_url}} {{branch_name}}`

- Extragerea unui nou istoric de proiect din istoria unui subarbore:

`git subtree split --prefix={{path/to/directory/}} {{repository_url}} -b {{branch_name}}`
