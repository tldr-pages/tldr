# oxlint

> High-performance JavaScript and TypeScript linter written in Rust.
> More information: <https://oxc.rs/docs/guide/usage/linter.html>.

- Lint all JavaScript and TypeScript files in the current directory:

`oxlint`

- Automatically fix auto-fixable lint problems:

`oxlint --fix`

- Deny a specific lint rule or category across the project:

`oxlint -D {{correctness|suspicious|perf}}`

- Lint a specific directory using a custom configuration file:

`oxlint -c {{path/to/oxlintrc.json}} {{src/}}`
