# git am

> Aplică fișiere patch și creează un commit. Util când se primesc commit-uri prin email.
> Vezi și: `exemplu`.
> Mai multe informații: <https://git-scm.com/docs/git-am>.

- Aplică și confirmă modificările urmând un fișier patch local:

`git am {{cale/către/fișier.patch}}`

- Aplică și confirmă modificările urmând un fișier patch la distanță:

`curl {{[-L|--location]}} {{https://example.com/file.patch}} | git am`

- Întrerupe procesul de aplicare a unui fișier patch:

`git am --abort`

- Aplică cât este posibil dintr-un fișier patch, salvând fragmentele eșuate în fișiere de respingere:

`git am --reject {{cale/către/fișier.patch}}`
