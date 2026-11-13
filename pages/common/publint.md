# publint

> Lint npm packages to ensure compatibility across Node.js, Vite, Webpack, Rollup, and TypeScript.
> More information: <https://publint.dev>.

- Lint the package in the current working directory:

`publint`

- Lint a specific package directory:

`publint {{path/to/package_directory}}`

- Specify the strictness level for reported issues:

`publint --level {{suggestion|warning|error}}`

- Check the package strictly without packing it first:

`publint --pack {{none}}`
