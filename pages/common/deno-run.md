# deno run

> Run a JavaScript or TypeScript program with the Deno runtime.
> More information: <https://docs.deno.com/runtime/reference/cli/run/>.

- Run a local JavaScript or TypeScript file:

`deno run {{path/to/file.ts}}`

- Run a remote script:

`deno run {{https://deno.land/std/examples/welcome.ts}}`

- Run a file with all permissions:

`deno run {{[-A|--allow-all]}} {{path/to/file.ts}}`

- Run a file with specific network and read permissions:

`deno run --allow-net={{example.com}} --allow-read={{/etc}} {{path/to/file.ts}}`

- Run a file and watch for changes:

`deno run --watch {{path/to/file.ts}}`

- Run a script with a specific `deno.json` configuration file:

`deno run {{[-c|--config]}} {{path/to/deno.json}} {{path/to/file.ts}}`

- Run a file and automatically download dependencies if they are missing:

`deno run --reload {{path/to/file.ts}}`
