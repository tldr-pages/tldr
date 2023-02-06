# az lock

> Azure-zárak kezelése. A `azure-cli` része. További információ: <https://learn.microsoft.com/cli/azure/lock>.

- Hozzon létre egy csak olvasható előfizetési szintű zárolást:

`az lock create --name {{lock_name}} --lock-type ReadOnly`

- Csak olvasható erőforráscsoport szintű zár létrehozása:

`az lock create --name {{lock_name}} --resource-group {{group_name}} --lock-type ReadOnly`

- Előfizetési szintű zár törlése:

`az lock delete --name {{lock_name}}`

- Erőforráscsoport szintű zár törlése:

`az lock delete --name {{lock_name}} --resource-group {{group_name}}`

- Az összes előfizetésszintű zárolás listázása:

`az lock list`

- Előfizetési szintű zárak megjelenítése:

`az lock show -n {{lock_name}}`
