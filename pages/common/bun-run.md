# bun run

> Execute a JavaScript/TypeScript file, or a script from `package.json`.
> More information: <https://bun.com/docs/cli/run>

- Run a script defined in `package.json`:

`bun run {{script_name}}`

- Run a JavaScript or TypeScript file directly:

`bun run {{path/to/file.ts}}`

- Run a file in "watch" mode (restarts automatically when the file changes):

`bun run --watch {{path/to/file.ts}}`

- Run a file using a specific configuration file:

`bun run --config {{path/to/bunfig.toml}} {{path/to/file.ts}}`
