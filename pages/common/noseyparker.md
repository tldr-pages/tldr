# noseyparker

> Scan text and Git history for secrets and sensitive information.
> Note: Use a separate datastore directory (`--datastore`) for each scan.
> See also: `trufflehog`.
> More information: <https://github.com/praetorian-inc/noseyparker#usage-examples>.

- Scan a local file or directory for secrets:

`noseyparker scan {{path/to/file_or_directory}} {{[-d|--datastore]}} {{path/to/datastore.np}}`

- Show a report from a previous scan:

`noseyparker report {{[-d|--datastore]}} {{path/to/datastore.np}}`

- Show a report in different format (default is `human`):

`noseyparker report {{[-d|--datastore]}} {{path/to/datastore.np}} {{[-f|--format]}} {{human|json|jsonl|sarif}}`

- Scan a remote Git repo (and Git history) for secrets:

`noseyparker scan --git-url {{URL}} {{[-d|--datastore]}} {{path/to/datastore.np}}`

- Scan all GitHub repositories of a user or organization for secrets:

`noseyparker scan {{--github-user|--github-organization}} {{username_or_org_name}} {{[-d|--datastore]}} {{path/to/datastore.np}}`

- List all scan rules:

`noseyparker rules list`

- List all GitHub repositories of a user or organization:

`noseyparker github repos list {{--user|--organization}} {{username_or_org_name}}`
