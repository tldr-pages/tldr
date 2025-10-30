# bun run

> Run a script from `package.json` using Bun.
> See also: `bun test`, `bun exec`.
> More information: <https://bun.com/docs/cli/run>.

- Run a script defined in `package.json`:

`bun run {{script_name}}`

- Pass arguments to the script (use `--` to forward arguments):

`bun run {{script_name}} -- {{arg1}} {{arg2}}`

- List available scripts:

`bun run`
