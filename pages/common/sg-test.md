# sg test

> Test ast-grep rules against test cases.
> More information: <https://ast-grep.github.io/reference/cli/test.html>.

- Run all rule tests:

`sg test`

- Run tests from a specific directory:

`sg test --test-dir {{path/to/test_directory}}`

- Update all snapshots that have changed:

`sg test --update-all`

- Interactively review and update snapshots:

`sg test --interactive`

- Only check if test code is valid without checking rule output:

`sg test --skip-snapshot-tests`

- Run only tests matching a regex filter:

`sg test --filter '{{regex_pattern}}'`
