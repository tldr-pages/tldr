# bun install

> Install JavaScript dependencies for a project from `package.json`.
> More information: <https://bun.com/docs/cli/install>.

- Install all dependencies listed in `package.json`:

`bun {{[i|install]}}`

- Install only production dependencies (skips `devDependencies`):

`bun {{[i|install]}} --production`

- Install dependencies exactly from the `bun.lockb` lockfile (frozen lockfile):

`bun install --frozen-lockfile`

- Force re-download all packages from the registry, ignoring the cache:

`bun install --force`

- Install a single package (this is an alias for `bun add`):

`bun install {{package_name}}`
