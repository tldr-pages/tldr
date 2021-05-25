# git remote

> Verwalte eine gewisse Anzahl an Repositories (remotes).
> Weitere Informationen: <https://git-scm.com/docs/git-remote>.

- Liste alle existierenden Remotes, ihre Namen und ihre URLs auf:

`git remote -v`

- Zeige Informationen über ein Remote an:

`git remote show {{remote_name}}`

- Füge ein neues Remote hinzu:

`git remote add {{remote_name}} {{remote_url}}`

- Ändere die URL eines Remotes (benutze `--add` um die existierende URL zu behalten):

`git remote set-url {{remote_name}} {{remote_url}}`

- Entferne ein Remote:

`git remote remove {{remote_name}}`

- Benenne ein Remote um:

`git remote rename {{alter_name}} {{neuer_name}}`
