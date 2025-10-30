# bun test

> Run tests using Bun's built-in test runner.
> It is a fast, Jest-compatible test runner that looks for `*.test.ts` (and similar) files.
> More information: <https://bun.com/docs/cli/test>

- Run all test files found in the project:

`bun test`

- Run a specific test file or directory:

`bun test {{path/to/file.test.ts}}`

- Run tests in "watch" mode (re-runs automatically on file changes):

`bun test --watch`

- Run tests and generate a code coverage report:

`bun test --coverage`
