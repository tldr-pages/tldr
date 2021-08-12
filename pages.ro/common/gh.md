# gh

> Lucrați fără probleme cu GitHub din linia de comandă.
> Mai multe informaţii: <https://cli.github.com/>

- Clonează un depozit GitHub local:

`gh repo clone {{owner}}/{{repository}}`

- Creați o nouă problemă:

`gh issue create`

- Vizualizați și filtrați problemele deschise ale depozitului curent:

`gh issue list`

- Vizualizați o problemă în browser:

`gh issue view --web {{issue_number}}`

- Creați o solicitare de tragere:

`gh pr create`

- Vizualizați o solicitare de tragere în browser:

`gh pr view --web {{pr_number}}`

- Verificați local sucursala unei cereri de tragere, având în vedere numărul său:

`gh pr checkout {{pr_number}}`

- Verificați starea solicitărilor de extragere ale unui depozit:

`gh pr status`
