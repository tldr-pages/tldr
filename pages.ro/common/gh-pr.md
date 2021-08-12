# gh pr

> Gestionați solicitările de extragere GitHub din linia de comandă.
> Mai multe informaţii: <https://cli.github.com/manual/gh_pr>

- Creați o solicitare de tragere:

`gh pr create`

- Check out o cerere de tragere la nivel local:

`gh pr checkout {{pr_number}}`

- Vizualizați modificările efectuate în PR:

`gh pr diff`

- Aprobarea cererii de tragere a sucursalei curente:

`gh pr review --approve`

- Îmbinați solicitarea de tragere asociată sucursalei curente interactiv:

`gh pr merge`

- Editați o solicitare de tragere interactiv:

`gh pr edit`

- Editați ramura de bază a unei cereri de tragere:

`gh pr edit --base {{branch_name}}`
