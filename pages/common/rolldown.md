# rolldown

> Fast Rust-based bundler for JavaScript and TypeScript with Rollup-compatible API.
> More information: <https://rolldown.rs/>.

- Bundle an entry file into an output directory:

`rolldown {{src/index.ts}} --dir {{dist}}`

- Bundle using a configuration file:

`rolldown -c {{rolldown.config.mjs}}`

- Watch source files and rebuild on changes:

`rolldown -c --watch`

- Bundle for a specific target platform and module format:

`rolldown {{src/index.ts}} --platform {{node|browser}} --format {{esm|cjs}} --dir {{dist}}`
