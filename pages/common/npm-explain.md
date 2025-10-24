# npm explain

> Explain how a package is installed, detailing its dependencies and reasons for inclusion.
> More information: <https://docs.npmjs.com/cli/explain>.

- Explain why a specific package is installed:

`npm explain {{package_name}}`

- Show explanation in JSON format:

`npm explain {{package_name}} --json`

- Include peer dependencies in the explanation:

`npm explain {{package_name}} --include {{peer}}`

- Limit explanation depth (e.g., 2 levels deep):

`npm explain {{package_name}} --depth {{2}}`
