# opengrep

> Static code analysis engine that matches code patterns and tracks data flow across functions and files.
> More information: <https://opengrep.dev/docs>.

- Scan a file or directory with rules from Semgrep's community repository:

`opengrep scan {{[-f|--config]}} auto {{path/to/file_or_directory}}`

- Scan with rules from a YAML file or a directory of YAML files:

`opengrep scan {{[-f|--config]}} {{path/to/rules_file_or_directory}} {{path/to/file_or_directory}}`

- Search for a code pattern in files of a specific language (`$X` matches any expression):

`opengrep scan {{[-e|--pattern]}} '{{eval($X)}}' {{[-l|--lang]}} {{python}} {{path/to/file_or_directory}}`

- Print the findings in a specific format:

`opengrep scan {{[-f|--config]}} {{path/to/rules_file_or_directory}} {{--json|--sarif|--junit-xml|--gitlab-sast|...}} {{path/to/file_or_directory}}`

- Report only the findings introduced after a specific commit in Git history:

`opengrep scan {{[-f|--config]}} {{path/to/rules_file_or_directory}} --baseline-commit {{commit}} {{path/to/file_or_directory}}`

- Scan the current Git repository in CI, reporting only the findings introduced by the pull request:

`opengrep ci {{[-f|--config]}} {{path/to/rules_file_or_directory}}`

- Track tainted data across files for taint rules that set `taint_interfile: true`:

`opengrep scan {{[-f|--config]}} {{path/to/rules_file_or_directory}} --enable-interfile {{path/to/directory}}`

- Set the number of parallel jobs, the timeout in seconds per rule and file, and the maximum file size:

`opengrep scan {{[-f|--config]}} {{path/to/rules_file_or_directory}} {{[-j|--jobs]}} {{4}} --timeout {{10}} --max-target-bytes {{2MB}} {{path/to/file_or_directory}}`
