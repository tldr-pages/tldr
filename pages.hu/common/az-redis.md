# az redis

> A Redis gyorsítótárak kezelése. A `azure-cli` része. További információ: <https://docs.microsoft.com/cli/azure/redis>.

- Hozzon létre egy új Redis gyorsítótár-példányt:

`az redis create --location {{location}} --name {{name}} --resource-group {{resource_group}} --sku {{Basic|Premium|Standard}} --vm-size {{c0|c1|c2|c3|c4|c5|c6|p1|p2|p3|p4|p5}}`

- Redis gyorsítótár frissítése:

`az redis update --name {{name}} --resource-group {{resource_group}} --sku {{Basic|Premium|Standard}} --vm-size {{c0|c1|c2|c3|c4|c5|c6|p1|p2|p3|p4|p5}}`

- A Redis gyorsítótárban tárolt adatok exportálása:

`az redis export --container {{container}} --file-format {{file-format}} --name {{name}} --prefix {{prefix}} --resource-group {{resource_group}}`

- Redis gyorsítótár törlése:

`az redis delete --name {{name}} --resource-group {{resource_group}} --yes`
