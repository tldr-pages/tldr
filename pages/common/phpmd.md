# phpmd

> A PHP mess detector that checks for common potential problems.
> More information: <https://github.com/phpmd/phpmd>.

- Display a list of available rulesets and formats:

`phpmd`

- Scan a file or directory for problems using comma-separated rulesets:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}}`

- Specify the minimum priority threshold for rules:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}} --minimumpriority {{priority}}`

- Include only the specified extensions in analysis:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}} --suffixes {{extensions}}`

- Exclude the specified comma-separated directories:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}} --exclude {{directory_patterns}}`

- Output the results to a file instead of stdout:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}} --reportfile {{path/to/report_file}}`

- Ignore the use of warning-suppressive PHPDoc comments:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}} --strict`
