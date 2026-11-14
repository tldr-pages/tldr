# vue-tsc

> Type-check Vue Single-File Components and TypeScript files from the command line using Volar.
> More information: <https://github.com/vuejs/language-tools>.

- Type-check the current Vue project without emitting JavaScript files:

`vue-tsc --noEmit`

- Type-check in watch mode and report errors continuously:

`vue-tsc --noEmit --watch`

- Generate TypeScript declaration files for a Vue component library:

`vue-tsc --declaration --emitDeclarationOnly`

- Type-check using a specific TypeScript configuration file:

`vue-tsc --project {{path/to/tsconfig.json}} --noEmit`
