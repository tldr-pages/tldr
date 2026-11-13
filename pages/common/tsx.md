# tsx

> Run TypeScript and ESM files seamlessly in Node.js without manual compilation.
> More information: <https://tsx.is/usage>.

- Execute a TypeScript or JavaScript file directly:

`tsx {{path/to/file.ts}}`

- Run a TypeScript file in watch mode, restarting automatically when imported files change:

`tsx watch {{path/to/file.ts}}`

- Start an interactive TypeScript REPL:

`tsx`

- Execute a script using a specific `tsconfig.json` file:

`tsx --tsconfig {{path/to/tsconfig.json}} {{path/to/file.ts}}`
