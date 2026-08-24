# git bundle

> Împachetează obiecte și referințe într-o arhivă.
> Mai multe informații: <https://git-scm.com/docs/git-bundle>.

- Creează un fișier bundle care conține toate obiectele și referințele unei ramuri specifice:

`git bundle create {{cale/către/fișier.bundle}} {{nume_ramură}}`

- Creează un fișier bundle pentru toate ramurile:

`git bundle create {{cale/către/fișier.bundle}} --all`

- Creează un fișier bundle cu ultimele 5 commit-uri ale ramurii curente:

`git bundle create {{cale/către/fișier.bundle}} -5 {{HEAD}}`

- Creează un fișier bundle cu ultimele 7 zile:

`git bundle create {{cale/către/fișier.bundle}} --since 7.days {{HEAD}}`

- Verifică dacă un fișier bundle este valid și poate fi aplicat la repository-ul curent:

`git bundle verify {{cale/către/fișier.bundle}}`

- Tipărește în `stdout` lista de referințe conținute într-un bundle:

`git bundle unbundle {{cale/către/fișier.bundle}}`

- Despachetează o ramură specifică dintr-un fișier bundle în repository-ul curent:

`git pull {{cale/către/fișier.bundle}} {{nume_ramură}}`

- Creează un repository nou dintr-un bundle:

`git clone {{cale/către/fișier.bundle}}`
