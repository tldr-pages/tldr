# npm ls

> Print installed packages to `stdout`.
> More information: <https://docs.npmjs.com/cli/npm-ls>.

- Print all versions of direct dependencies in the current project to `stdout`:

`npm {{[ls|list]}}`

- Print all installed packages including peer dependencies:

`npm {{[ls|list]}} {{[-a|--all]}}`

- Print all globally installed packages:

`npm {{[ls|list]}} {{[-g|--global]}}`

- Print dependencies with extended information:

`npm {{[ls|list]}} {{[-l|--long]}}`

- Print dependencies in parseable format:

`npm {{[ls|list]}} {{[-p|--parseable]}}`

- Print dependencies in JSON format:

`npm {{[ls|list]}} --json`
