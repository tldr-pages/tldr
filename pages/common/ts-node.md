# ts-node

> Run TypeScript code directly, without any compiling.
> More information: <https://www.npmjs.com/package/ts-node>.

- Execute a TS file without compiling (`node` + `tsc`).

`ts-node {{path/to/file.ts}}`

- Execute a TS file without loading `tsconfig.json`:

`ts-node --skip-project {{path/to/file.ts}}`

- Display TS-Node help:

`ts-node --help`

- Eval TS Code directly on the terminal

`ts-node -e 'console.log("Hello World")'`

- Run code in Script Mode for `foobar.ts`

`ts-node --script-mode {{foobar.ts}}`

- Only transpile the TS File `foobar.ts` to JS

`ts-node --transpile-only {{foobar.ts}}`
