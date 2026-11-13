# tsup

> Bundle TypeScript libraries with zero configuration, powered by esbuild.
> More information: <https://tsup.egoist.dev/>.

- Bundle one or more entry files into the default `dist` directory:

`tsup {{src/index.ts}}`

- Bundle for both CommonJS and ECMAScript Module formats and generate `.d.ts` declaration files:

`tsup {{src/index.ts}} --format {{cjs,esm}} --dts`

- Watch source files for changes and rebuild automatically:

`tsup {{src/index.ts}} --watch`

- Minify the output bundle and clean the output directory before building:

`tsup {{src/index.ts}} --minify --clean`
