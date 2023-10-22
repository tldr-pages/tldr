# ts-node

> Run TypeScript code directly, without any compiling.
> More information: <https://typestrong.org/ts-node>.

- Execute a TypeScript file without compiling (`node` + `tsc`):

`ts-node {{path/to/file.ts}}`

- Execute a TypeScript file without loading `tsconfig.json`:

`ts-node --skip-project {{path/to/file.ts}}`

- Evaluate TypeScript code passed as a literal:

`ts-node --eval '{{console.log("Hello World")}}'`

- Execute a TypeScript file in script mode:

`ts-node --script-mode {{path/to/file.ts}}`

- Transpile a TypeScript file to JavaScript without executing it:

`ts-node --transpile-only {{path/to/file.ts}}`

- Display TS-Node help:

`ts-node --help`
