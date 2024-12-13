# vitest

> Fast, modern testing framework built for Vite, offering seamless integration, TypeScript support, and a Jest-compatible API for unit, integration, and snapshot testing.
> More information: <https://vitest.dev/guide>.

- Run all available tests:

`vitest run`

- Run the test suites from the given files:

`vitest run {{path/to/file1 path/to/file2 ...}}`

- Run the test suites from files within the current and subdirectories, whose paths match the given regular expression:

`vitest run {{regular_expression1}} {{regular_expression2}}`

- Run the tests whose names match the given regular expression:

`vitest run --testNamePattern {{regular_expression}}`

- Watch files for changes and automatically re-run related tests:

`vitest`

- Run tests with coverage:

`vitest run --coverage`

- Run all tests but stops immediately after the first test failure:

`vitest run --bail=1`

- Display help:

`vitest --help`
