# git bulk

> Műveletek végrehajtása több Git-tárhelyen. A `git-extras` része. További információ: <https://github.com/tj/git-extras/blob/master/Commands.md#git-bulk>.

- Az aktuális könyvtár munkaterületként való regisztrálása:

`git bulk --addcurrent {{workspace_name}}`

- Munkatér regisztrálása tömeges műveletekhez:

`git bulk --addworkspace {{workspace_name}} {{/absolute/path/to/repository}}`

- Egy adott könyvtáron belüli tároló klónozása, majd a tároló munkaterületként való regisztrálása:

`git bulk --addworkspace {{workspace_name}} {{/absolute/path/to/parent_directory}} --from {{remote_repository_location}}`

- Tárházak klónozása távoli helyek újsorral elválasztott listájából, majd munkaterületként való regisztrálása:

`git bulk --addworkspace {{workspace-name}} {{absolute/path/to/root/directory}} --from {{absolute/path/to/file}}`

- Az összes regisztrált munkaterület listázása:

`git bulk --listall`

- Git parancs futtatása az aktuális munkaterület tárolóin:

`git bulk {{command}} {{command_arguments}}`

- Egy adott munkaterület eltávolítása:

`git bulk --removeworkspace {{workspace_name}}`

- Az összes munkaterület eltávolítása:

`git bulk --purge`
