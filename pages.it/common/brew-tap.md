# brew tap

> Aggiungi un repository di formule Homebrew. Se non vengono forniti argomenti, elenca tutti i tap Homebrew installati.
> Maggiori informazioni: <https://docs.brew.sh/Manpage#tap-options-userrepo-url>.

- Elenca i tap Homebrew installati:

`brew tap`

- Aggiungi un repository Git ospitato su GitHub:

`brew tap {{nome_utente_github}}/{{nome_repository_github}}`

- Aggiungi un repository Git ospitato fuori da GitHub:

`brew tap {{nome_utente}}/{{nome_repository}} {{url_git_clone}}`

- Aggiungi un repository ospitato su GitLab:

`brew tap {{nome_utente}}/{{nome_repository}} https://gitlab.com/{{nome_utente}}/{{nome_repository}}.git`

- Mostra l'aiuto:

`brew tap {{[-h|--help]}}`
