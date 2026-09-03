# rumdl

> A fast Markdown linter and formatter written in Rust.
> More information: <https://rumdl.dev>.

- Lint the specified files or directories:

`rumdl check {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Lint and automatically fix issues where possible:

`rumdl check {{[-f|--fix]}} {{path/to/file_or_directory}}`

- Lint with specific rules disabled:

`rumdl check {{[-d|--disable]}} {{rule_id1,rule_id2,...}} {{path/to/file_or_directory}}`

- Re-run the linter whenever files change:

`rumdl check {{[-w|--watch]}} {{path/to/file_or_directory}}`

- Format files in place:

`rumdl fmt {{path/to/file_or_directory}}`

- Create a default configuration file (`.rumdl.toml`) in the current directory:

`rumdl init`

- Show information about a specific rule (omit the rule to list all rules):

`rumdl rule {{MD013}}`

- Display version:

`rumdl version`
