# gitleaks

> Detect secrets and API keys leaked in Git repositories.
> More information: <https://github.com/gitleaks/gitleaks>.

- Scan a remote repository:

`gitleaks detect --repo-url {{https://github.com/username/repository.git}}`

- Scan a local directory:

`gitleaks detect --source {{path/to/repository}}`

- Output scan results to a JSON file:

`gitleaks detect --source {{path/to/repository}} --report {{path/to/report.json}}`

- Use a custom rules file:

`gitleaks detect --source {{path/to/repository}} --config-path {{path/to/config.toml}}`

- Start scanning from a specific commit:

`gitleaks detect --source {{path/to/repository}} --log-opts {{--since=commit_id}}`

- Scan uncommitted changes before a commit:

`gitleaks protect --staged`

- Display verbose output indicating which parts were identified as leaks during the scan:

`gitleaks protect --staged --verbose`
