# brew tap

> Aggiungi un repository di formule Homebrew. Se non vengono forniti argomenti, elenca tutti i tap Homebrew installati.
> Maggiori informazioni: <https://docs.brew.sh/Manpage#tap-options-userrepo-url>.

- Elenca i tap Homebrew installati:

`brew tap`

- Aggiungi un repository Git ospitato su GitHub:

`brew tap {{github_username}}/{{github_repository_name}}`

- Aggiungi un repository Git ospitato fuori da GitHub:

`brew tap {{username}}/{{repository_name}} {{git_clone_url}}`

- Aggiungi un repository ospitato su GitLab:

`brew tap {{username}}/{{repository_name}} https://gitlab.com/{{username}}/{{repository_name}}.git`

- Mostra l'aiuto:

`brew tap {{[-h|--help]}}`
