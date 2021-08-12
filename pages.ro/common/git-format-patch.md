# git format-patch

> Pregătiți fișierele.patch. Util atunci când trimiterea prin e-mail se angajează în altă parte.
> A se vedea, de asemenea, `git am`, care poate aplica fișiere.patch generate.
> Mai multe informaţii: <https://git-scm.com/docs/git-format-patch>

- Creați un fișier `.patch` numit automat pentru toate angajările neîmpinse:

`git format-patch {{origin}}`

- Scrieți un fișier `.patch` pentru toate angajările între 2 revizuiri la stdout:

`git format-patch {{revision_1}}..{{revision_2}}`

- Scrieți un fișier `.patch` pentru cele mai recente 3 angajări:

`git format-patch -{{3}}`
