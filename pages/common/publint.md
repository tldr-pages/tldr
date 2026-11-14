# publint

> Lint npm packages to ensure wide compatibility across environments like Vite, Webpack, Rollup, and Node.js.
> More information: <https://publint.dev/>.

- Lint the package in the current directory:

`publint`

- Lint a package in a specific directory:

`publint {{path/to/package_directory}}`

- Specify the minimum severity level of messages to report:

`publint --level {{suggestion|warning|error}}`

- Fail with a non-zero exit code on warnings as well as errors:

`publint --strict`
