# bun build

> Bundle JavaScript and TypeScript files with Bun's fast native bundler.
> More information: <https://bun.com/docs/bundler>.

- Bundle an entry point to a single output file:

`bun build {{path/to/entry.ts}} --outfile {{path/to/output.js}}`

- Bundle multiple entry points to an output directory:

`bun build {{path/to/entry1.ts path/to/entry2.ts ...}} --outdir {{path/to/dist}}`

- Bundle with source maps for debugging:

`bun build {{path/to/entry.ts}} --outfile {{path/to/output.js}} --sourcemap`

- Bundle with minification for production:

`bun build {{path/to/entry.ts}} --outfile {{path/to/output.js}} --minify`

- Bundle with a specific target environment:

`bun build {{path/to/entry.ts}} --outfile {{path/to/output.js}} --target {{browser|bun|node}}`

- Bundle to a standalone executable:

`bun build {{path/to/entry.ts}} --compile --outfile {{path/to/executable}}`

- Watch for file changes and rebuild automatically:

`bun build {{path/to/entry.ts}} --outfile {{path/to/output.js}} --watch`

- Bundle with external dependencies not included in the output:

`bun build {{path/to/entry.ts}} --outfile {{path/to/output.js}} --external {{react react-dom}}`
