# gh gist

> Lucrul cu GitHub Gists în linia de comandă.
> Mai multe informaţii: <https://cli.github.com/manual/gh_gist>

- Creați un Gist nou dintr-o listă de fișiere separate de spațiu:

`gh gist create {{path/to/files}}`

- Creați un nou Gist cu o descriere:

`gh gist create {{filename}} --desc "{{description}}"`

- Editează o Gist:

`gh gist edit {{id_or_url}}`

- Lista Gists deţinută de utilizatorul autentificat în prezent:

`gh gist list --limit {{int}}`

- Vizualizați un Gist în browserul implicit fără a reda Markdown:

`gh gist view {{id_or_url}} --web --raw`
