# npm pack

> Create a tarball from a package.
> More information: <https://docs.npmjs.com/cli/pack>.

- Create a tarball from the current package in the current directory:

`npm pack`

- Create a tarball from a specific package folder:

`npm pack path/to/package_folder`

- Run a dry run to preview the tarball contents without creating it:

`npm pack --dry-run`

- Create a tarball without running lifecycle scripts:

`npm pack --ignore-scripts`

- Specify a custom registry to fetch package metadata from:

`npm pack --registry https://registry.npmjs.org/`
