# sherif

> Zero-config, fast Rust-based linter for JavaScript and TypeScript monorepos.
> More information: <https://github.com/QuiiBz/sherif>.

- Lint the current monorepo for dependency, version, and package manifest issues:

`sherif`

- Automatically fix all auto-fixable monorepo issues:

`sherif --fix`

- Ignore a specific rule during linting:

`sherif --ignore-rule {{multiple-dependency-versions}}`

- Ignore specific workspace packages during linting:

`sherif --ignore-package {{package_name}}`
