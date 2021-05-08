# ts-node

> Run TypeScript code directly, without any compiling.
> More information: <https://www.npmjs.com/package/ts-node>.

- Execute a TS File `foobar.ts` without compiling ('node' + 'tsc')

`ts-node {{foobar.ts}}`

- TS-Node Loads tsconfig.json by default. To prevent that

`ts-node --skip-project {{foobar.ts}}`

- Loads TS-Node Help

`ts-node --help`

- Eval TS Code directly on the terminal

`ts-node -e 'console.log("Hello World")'`

- Run code in Script Mode for `foobar.ts`

`ts-node --script-mode {{foobar.ts}}`

- Only transpile the TS File `foobar.ts` to JS

`ts-node --transpile-only {{foobar.ts}}`
