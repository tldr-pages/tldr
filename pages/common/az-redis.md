# az redis

> Manage Redis caches.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/redis>.

- Create a new Redis cache instance:

`az redis create --location {{location}} {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}} --sku {{Basic|Premium|Standard}} --vm-size {{c0|c1|c2|c3|c4|c5|c6|p1|p2|p3|p4|p5}}`

- Update a Redis cache:

`az redis update {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}} --sku {{Basic|Premium|Standard}} --vm-size {{c0|c1|c2|c3|c4|c5|c6|p1|p2|p3|p4|p5}}`

- Export data stored in a Redis cache:

`az redis export --container {{container}} --file-format {{file-format}} {{[-n|--name]}} {{name}} --prefix {{prefix}} {{[-g|--resource-group]}} {{resource_group}}`

- Delete a Redis cache:

`az redis delete {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}} {{[-y|--yes]}}`
