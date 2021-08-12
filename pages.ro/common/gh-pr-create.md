# gh pr create

> Gestionați solicitările de extragere GitHub din linia de comandă.
> Mai multe informaţii: <https://cli.github.com/manual/gh_pr_create>

- Creați interactiv o solicitare de tragere:

`gh pr create`

- Creați o solicitare de tragere, determinând titlul și descrierea din mesajele de comitere ale sucursalei curente:

`gh pr create --fill`

- Creați o solicitare de tragere a proiectului:

`gh pr create --draft`

- Creați o solicitare de tragere specificând ramura de bază, titlul și descrierea:

`gh pr create --base {{base_branch}} --title "{{title}}" --body "{{body}}"`

- Începeți să deschideți o solicitare de tragere în browser:

`gh pr create --web`
