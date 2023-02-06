# az sshkey

> Az ssh nyilvános kulcsok kezelése virtuális gépekkel. A `azure-cli` része. További információ: <https://learn.microsoft.com/cli/azure/sshkey>.

- Hozzon létre egy új SSH-kulcsot:

`az sshkey create --name {{name}} --resource-group {{resource_group}}`

- Egy meglévő SSH-kulcs feltöltése:

`az sshkey create --name {{name}} --resource-group {{resource_group}} --public-key "{{@path/to/key.pub}}"`

- Az összes SSH nyilvános kulcs listázása:

`az sshkey list`

- Információk megjelenítése egy SSH nyilvános kulcsról:

`az sshkey show --name {{name}} --resource-group {{resource_group}}`
