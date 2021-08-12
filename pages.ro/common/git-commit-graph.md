# git commit-graph

> Scrieți și verificați fișierele de grafice de comitet Git.
> Mai multe informaţii: <https://git-scm.com/docs/git-commit-graph>

- Scrieți un fișier de comitet pentru angajamentele ambalate în directorul local `.git` al depozitului:

`git commit-graph write`

- Scrieți un fișier grafic de comitet care conține toate angajamentele accesibile:

`git show-ref --hash | git commit-graph write --stdin-commits`

- Scrieți un fișier de comitet care conține toate angajamentele din fișierul grafic de comitet curent, împreună cu cele care pot fi accesate de la „CAPT”:

`git rev-parse {{HEAD}} | git commit-graph write --stdin-commits --append`
