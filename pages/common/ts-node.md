# ts-node

> Run TypeScript code directly, without any compiling.
> More information: <https://www.npmjs.com/package/ts-node>.

- Execute a TypeScript file without compiling (`node` + `tsc`).

`ts-node {{path/to/file.ts}}`

- Execute a TypeScript file without loading `tsconfig.json`:

`ts-node --skip-project {{path/to/file.ts}}`

- Display TS-Node help:

`ts-node --help`

- Evaluate TypeScript code directly on the terminal:

`ts-node -e '{{console.log("Hello World")}}'`

- Execute a TypeScript file in script mode:

`ts-node --script-mode {{path/to/file.ts}}`

- Only transpile the TypeScript File `foobar.ts` to JavaScript

`ts-node --transpile-only {{foobar.ts}}`
