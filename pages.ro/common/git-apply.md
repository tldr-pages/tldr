# git apply

> Aplică un patch la fișiere și/sau la index fără a crea un commit.
> Vezi și: `git am`.
> Mai multe informații: <https://git-scm.com/docs/git-apply>.

- Afișează mesaje despre fișierele patch-uite:

`git apply {{[-v|--verbose]}} {{cale/către/fișier}}`

- Aplică și adaugă fișierele patch-uite la index:

`git apply --index {{cale/către/fișier}}`

- Aplică un fișier patch de la distanță:

`curl {{[-L|--location]}} {{https://exemplu.com/fișier.patch}} | git apply`

- Afișează diffstat pentru input și aplică patch-ul:

`git apply --stat --apply {{cale/către/fișier}}`

- Aplică patch-ul în sens invers:

`git apply {{[-R|--reverse]}} {{cale/către/fișier}}`

- Stochează rezultatul patch-ului în index fără a modifica working tree-ul:

`git apply --cache {{cale/către/fișier}}`
