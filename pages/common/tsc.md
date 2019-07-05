# tsc

> TypeScript compiler.
> More information: <https://www.typescriptlang.org/docs/handbook/compiler-options.html>.

- Compile a TypeScript file `foobar.ts` into a JavaScript file `foobar.js`:

`tsc {{foobar.ts}}`

- Compile a TypeScript file into JavaScript using a specific target syntax (default is `ES3`):

`tsc --target {{ES5|ES2015|ES2016|ES2017|ES2018|ESNEXT}} {{foobar.ts}}`

- Compile a TypeScript file into a JavaScript file with a custom name:

`tsc --outFile {{output.js}} {{input.ts}}`

- Get command line options and files from a file:

`tsc @{{args.txt}}`

- Compile a TypeScript project if outdated:

`tsc --build {{tsconfig.json}}`

- Type-check JavaScript files and output only the errors:

`tsc --allowJs --checkJs --noEmit {{src/**/*.js}}`
