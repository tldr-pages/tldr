# bun build

> Bundle and transpile code with Bun.
> More information: <https://bun.com/docs/bundler>.

- Build an entry point to an output directory:

`bun build {{src/index.ts}} --outdir {{dist}}`

- Build and minify output:

`bun build {{src/index.ts}} --outdir {{dist}} --minify`

- Watch files and rebuild on changes:

`bun build {{src/index.ts}} --outdir {{dist}} --watch`
