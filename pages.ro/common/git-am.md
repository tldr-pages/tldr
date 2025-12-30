# git am

> Aplică fișiere patch. Util când se primesc commit-uri prin email.
> Vezi și `git format-patch` pentru generarea fișierelor patch.
> Mai multe informații: <https://git-scm.com/docs/git-am>.

- Aplică un fișier patch:

`git am {{cale/către/fișier.patch}}`

- Întrerupe aplicarea unui fișier patch:

`git am --abort`

- Aplică cât este posibil dintr-un fișier patch, salvând părțile neaplicabile în fișiere `.rej`:

`git am --reject {{cale/către/fișier.patch}}`
