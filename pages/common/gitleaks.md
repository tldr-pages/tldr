# gitleaks

> Detect secrets and API keys leaked in Git repositories, directories, and files.
> More information: <https://github.com/gitleaks/gitleaks#usage>.

- Scan the commit history of the current Git repository and print each finding:

`gitleaks git {{[-v|--verbose]}}`

- Scan the commit history of a specific Git repository:

`gitleaks git {{path/to/repository}}`

- Scan staged changes before committing:

`gitleaks git --staged`

- Scan only a specific range of commits:

`gitleaks git --log-opts "{{start_commit}}..{{end_commit}}"`

- Scan a directory or file without looking at Git history:

`gitleaks dir {{path/to/file_or_directory}}`

- Scan data from `stdin`:

`cat {{path/to/file}} | gitleaks stdin`

- Write the findings to a report file in a specific format:

`gitleaks git {{[-r|--report-path]}} {{path/to/report}} {{[-f|--report-format]}} {{json|csv|junit|sarif}}`

- Use a custom configuration file and ignore findings already listed in a previous report:

`gitleaks git {{[-c|--config]}} {{path/to/config.toml}} {{[-b|--baseline-path]}} {{path/to/baseline.json}}`
