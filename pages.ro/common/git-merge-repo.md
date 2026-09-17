# git merge-repo

> Fuzionează două istorii de repository-uri.
> Face parte din `git-extras`.
> Mai multe informații: <https://github.com/tj/git-extras/blob/main/Commands.md#git-merge-repo>.

- Fuzionează o ramură a unui repository în directorul repository-ului curent:

`git merge-repo {{path/to/repo}} {{branch_name}} {{path/to/directory}}`

- Fuzionează o ramură a unui repository la distanță în directorul repository-ului curent, fără a păstra istoricul:

`git merge-repo {{path/to/remote_repo}} {{branch_name}} .`
