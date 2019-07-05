# tsc

> TypeScript compiler.
> More information: <https://www.typescriptlang.org/docs/handbook/compiler-options.html>.

- Compile a TypeScript file `hello.ts` into a JavaScript file `hello.js`:

`tsc {{foo.ts}}`

- Compile a TypeScript file into JavaScript using a specific target syntax (default is `ES3`):

`tsc --target {{ES5|ES2015|ES2016|ES2017|ES2018|ESNEXT}} {{foo.ts}}`

- Compile a TypeScript file into a JavaScript file with a custom name:

`tsc --outFile {{foo.js}} {{bar.ts}}`

- Get command line options and files from a file:

`tsc @{{args.txt}}`

- Compile a TypeScript project if outdated:

`tsc --build {{tsconfig.json}}`

- Type-check JavaScript files and output only the errors:

`tsc --allowJs --checkJs --noEmit {{src/**/*.js}}`
