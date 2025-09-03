# tsc

> TypeScript compiler.
> More information: <https://www.typescriptlang.org/docs/handbook/compiler-options.html>.

- Initialize a TypeScript project:

`tsc --init`

- Compile a TypeScript file `foobar.ts` into a JavaScript file `foobar.js`:

`tsc {{foobar.ts}}`

- Compile a TypeScript file into JavaScript using a specific target syntax (default is `ES3`):

`tsc {{[-t|--target]}} {{ES5|ES2015|ES2016|ES2017|ES2018|ESNEXT|...}} {{foobar.ts}}`

- Compile a TypeScript file into a JavaScript file with a custom name:

`tsc --outFile {{output.js}} {{input.ts}}`

- Compile all `.ts` files of a TypeScript project defined in a `tsconfig.json` file (`--build` can be omitted to build the project in the current working directory):

`tsc {{[-b|--build]}} {{tsconfig.json}}`

- Run the compiler using command-line options and arguments fetched from a text file:

`tsc @{{args.txt}}`

- Type-check multiple JavaScript files, and output only the errors:

`tsc --allowJs --checkJs --noEmit {{src/**/*.js}}`

- Run the compiler in watch mode, which automatically recompiles code when it changes:

`tsc {{[--watch]}}`
