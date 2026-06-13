# bun pm

> A set of utilities for working with Bun's package manager.
> Some subcommands such as `pack`, `pkg` have their own usage documentation.
> More information: <https://bun.com/docs/pm/cli/pm>.

- Create a tarball of the current workspace:

`bun pm pack`

- Print the path to the `bin` directory:

`bun pm bin`

- Display the default trusted dependencies:

`bun pm default-trusted`

- Print the npm registry username:

`bun pm whoami`

- Generate and print the hash of the current lockfile:

`bun pm hash`

- List the current untrusted dependencies that contain scripts:

`bun pm untrusted`

- Migrate another package manager's lockfile without installing anything:

`bun pm migrate`

- Get a property from `package.json`:

`bun pm pkg get {{property}}`
