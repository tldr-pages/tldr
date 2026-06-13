# git annotate

> Afișează hash-ul commit-ului și ultimul autor pe fiecare linie a unui fișier.
> Vezi `git blame`, care este preferat față de `git annotate`.
> `git annotate` este oferit pentru cei familiarizați cu alte sisteme de control al versiunilor.
> Mai multe informații: <https://git-scm.com/docs/git-annotate>.

- Afișează un fișier cu numele autorului și hash-ul commit-ului adăugat la începutul fiecărei linii:

`git annotate {{cale/către/fișier}}`

- Afișează un fișier cu email-ul autorului și hash-ul commit-ului adăugat la începutul fiecărei linii:

`git annotate {{[-e|--show-email]}} {{cale/către/fișier}}`

- Afișează doar rândurile care se potrivesc cu un `regex`:

`git annotate -L :{{regexp}} {{cale/către/fișier}}`
