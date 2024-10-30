# npm cache

> Manage the npm package cache.
> More information: <https://docs.npmjs.com/cli/commands/npm-cache>.

- Add a specific package to the cache:

`npm cache add {{package_name}}`

- Remove a specific package from the cache:

`npm cache remove {{package_name}}`

- Clear a specific cached item by key:

`npm cache clean {{key}}`

- Clear the entire npm cache:

`npm cache clean --force`

- List the contents of the npm cache:

`npm cache ls`

- Verify the integrity of the npm cache:

`npm cache verify`

- Show information about the npm cache location and configuration:

`npm cache dir`

- Change the cache path:

`npm config set cache {{path/to/directory}}`
