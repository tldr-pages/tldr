# git remote

> Verwalte die Menge an verfolgten Repositories (genannt "remotes").
> Mehr Informationen: <https://git-scm.com/docs/git-remote>.

- Liste die existierenden Remotes, ihre Namen und ihre URLs auf:

`git remote -v`

- Zeige Informationen über ein Remote an:

`git remote show {{name_des_remotes}}`

- Füge ein Remote hinzu:

`git remote add {{name_des_remotes}} {{url_des_remotes}}`

- Ändere die URL eines Remotes (benutze `--add` um die existierende URL zu behalten):

`git remote set-url {{name_des_remotes}} {{url_des_remotes}}`

- Entferne ein Remote:

`git remote remove {{name_des_remotes}}`

- Benenne ein Remote um:

`git remote rename {{alter_name}} {{neuer_name}}`
