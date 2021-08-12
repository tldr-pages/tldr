# git am

> Aplicați fișierele de corecție. Utile la primirea de angajări prin e-mail.
> A se vedea, de asemenea, `git format-patch`, care poate genera fișiere de patch-uri.
> Mai multe informaţii: <https://git-scm.com/docs/git-am>

- Aplicați un fișier de patch-uri:

`git am {{path/to/file.patch}}`

- Abandonați procesul de aplicare a unui fișier de patch-uri:

`git am --abort`

- Aplicați cât mai mult posibil un fișier de patch-uri, salvând bucăți eșuate pentru a respinge fișierele:

`git am --reject {{path/to/file.patch}}`
