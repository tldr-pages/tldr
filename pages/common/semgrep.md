# semgrep

> Perform *static source code analysis* (SAST) on your source code to detect security vulnerabilities.
> Semgrep is a fast SAST tool aiming to minimize false positives.
> More information: <https://semgrep.dev/>.

- Run semgrep on a source directory, automatically detecting matching rules:

`semgrep --config=auto {{path/to/directory}}`

- Run semgrep on a source directory, manually selecting the desired rulesets:

`semgrep --config p/{{ruleset_name}} [--config p/{{another_ruleset_name}} ...] {{sourcecode_path}}`

- Run semgrep within a Docker container on the current directory:

`docker run --rm -v "${PWD}:/src" returntocorp/semgrep [--config p/{{ruleset_name}} ...]`
