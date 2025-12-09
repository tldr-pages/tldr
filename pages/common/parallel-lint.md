# parallel-lint

> Check the syntax of PHP files in parallel.
> More information: <https://github.com/JakubOnderka/PHP-Parallel-Lint>.

- Lint a specific directory:

`parallel-lint {{path/to/directory}}`

- Lint a directory using the specified number of parallel processes:

`parallel-lint -j {{processes}} {{path/to/directory}}`

- Lint a directory, excluding the specified directory:

`parallel-lint --exclude {{path/to/excluded_directory}} {{path/to/directory}}`

- Lint a directory of files using a comma-separated list of extension(s):

`parallel-lint -e {{php,html,phpt}} {{path/to/directory}}`

- Lint a directory and output the results as JSON:

`parallel-lint --json {{path/to/directory}}`

- Lint a directory and show Git Blame results for rows containing errors:

`parallel-lint --blame {{path/to/directory}}`
