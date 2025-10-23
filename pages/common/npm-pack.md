# npm-pack

> Create a tarball from a package.
> Useful for testing how your package will look if published, or to share it manually.
> More information: <https://docs.npmjs.com/cli/v10/commands/npm-pack>.

- Create a `.tgz` tarball from the current project:

`npm pack`

- Create a tarball from another package folder:

`npm pack {{path/to/package}}`

- Specify the registry to resolve dependencies when packing:

`npm pack --registry {{https://your.registry.url/}}`
