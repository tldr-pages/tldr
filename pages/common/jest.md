# jest

> A zero-configuration JavaScript testing platform.
> More information: <https://jestjs.io>.

- Run all available tests:

`jest`

- Run the test suites from the given files:

`jest {{path/to/file1 path/to/file2 ...}}`

- Run the test suites from files within the current and subdirectories, whose paths match the given `regex`:

`jest {{regex1}} {{regex2}}`

- Run the tests whose names match the given `regex`:

`jest --testNamePattern {{regex}}`

- Run test suites related to a given source file:

`jest --findRelatedTests {{path/to/source_file.js}}`

- Run test suites related to all uncommitted files:

`jest --onlyChanged`

- Watch files for changes and automatically re-run related tests:

`jest --watch`

- Display help:

`jest --help`
