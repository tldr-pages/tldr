# ts-node

> Run TypeScript code directly, without any compiling.
> More information: <https://www.npmjs.com/package/ts-node>.

- Execute a TS file without compiling (`node` + `tsc`).

`ts-node {{path/to/file.ts}}`

- Execute a TS file without loading `tsconfig.json`:

`ts-node --skip-project {{path/to/file.ts}}`

- Display TS-Node help:

`ts-node --help`

- Evaluate TS code directly on the terminal:

`ts-node -e '{{console.log("Hello World")}}'`

- Execute a TS file in script mode:

`ts-node --script-mode {{path/to/file.ts}}`

- Only transpile the TS File `foobar.ts` to JS

`ts-node --transpile-only {{foobar.ts}}`
