# phpmd

> PHP mess detector: check for common potential problems.
> More information: <https://github.com/phpmd/phpmd>.

- Display a list of available rulesets and formats:

`phpmd`

- Scan a file or directory for problems using comma-separated rulesets:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{ruleset1,ruleset2,...}}`

- Specify the minimum priority threshold for rules:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{ruleset1,ruleset2,...}} --minimumpriority {{priority}}`

- Include only the specified extensions in analysis:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{ruleset1,ruleset2,...}} --suffixes {{extensions}}`

- Exclude the specified comma-separated directories:

`phpmd {{path/to/file_or_directory1,path/to/file_or_directory2,...}} {{xml|text|html}} {{ruleset1,ruleset2,...}} --exclude {{directory_patterns}}`

- Output the results to a file instead of `stdout`:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{ruleset1,ruleset2,...}} --reportfile {{path/to/report_file}}`

- Ignore the use of warning-suppressive PHPDoc comments:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{ruleset1,ruleset2,...}} --strict`
