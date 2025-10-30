# bun install

> Install dependencies listed in `package.json` using Bun.
> See also: `bun add`, `bun remove`, `bun update`.
> More information: <https://bun.com/docs/cli/install>.

- Install dependencies in the current project:

`bun install`

- Install only production dependencies:

`bun install --production`

- Install without modifying the lockfile (fail if out of sync):

`bun install --frozen-lockfile`
