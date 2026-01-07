# npm cache

> Manage the npm package cache.
> More information: <https://docs.npmjs.com/cli/npm-cache/>.

- Add a specific package to the cache:

`npm cache add {{package_name}}`

- Clear a specific cached item by key:

`npm cache clean {{key}}`

- Clear the entire npm cache:

`npm cache clean {{[-f|--force]}}`

- List cached packages:

`npm cache ls`

- List cached packages matching a specific name and version:

`npm cache ls {{name}}@{{version}}`

- Verify the integrity of the npm cache:

`npm cache verify`

- List all entries in the npx cache:

`npm cache npx ls`
