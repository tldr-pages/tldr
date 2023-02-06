# az webapp

> Az Azure felhőszolgáltatásokban hosztolt webalkalmazások kezelése. A `azure-cli` webhely része. Móddal kapcsolatos információk: <https://learn.microsoft.com/cli/azure/webapp>.

- A webalkalmazás elérhető futási idejeinek listázása:

`az webapp list-runtimes --os-type {{windows|linux}}`

- Webalkalmazás létrehozása:

`az webapp up --name {{name}} --location {{location}} --runtime {{runtime}}`

- Az összes webalkalmazás listázása:

`az webapp list`

- Egy adott webalkalmazás törlése:

`az webapp delete --name {{name}} --resource-group {{resource_group}}`
