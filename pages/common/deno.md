# deno

> A secure runtime for JavaScript and TypeScript.
> More information: <https://deno.land/>.

- Run a JavaScript or TypeScript file:

`deno {{path/to/file.ts}}`

- Start a REPL (interactive shell):

`deno`

- Run a file with network access enabled:

`deno --allow-net {{path/to/file.ts}}`

- Run a file from a URL:

`deno {{https://deno.land/std/examples/welcome.ts}}`

- Install an executable script from a URL:

`deno install --allow-net --allow-read {{file_server}} {{https://deno.land/std/http/file_server.ts}}`
