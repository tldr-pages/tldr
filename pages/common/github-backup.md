# github-backup

> Back up the repositories, issues, pull requests, and other data of a GitHub user or organization.
> More information: <https://github.com/josegonzalez/python-github-backup>.

- Back up all data of a user to a specific directory, authenticating with a personal access token:

`github-backup {{username}} {{[-t|--token]}} {{token}} --all {{[-o|--output-directory]}} {{path/to/directory}}`

- Back up all data of a user, reading the token from the GitHub CLI:

`github-backup {{username}} --token-from-gh --all {{[-o|--output-directory]}} {{path/to/directory}}`

- Also include private and forked repositories:

`github-backup {{username}} --token-from-gh --all {{[-P|--private]}} {{[-F|--fork]}} {{[-o|--output-directory]}} {{path/to/directory}}`

- Back up all data of an organization:

`github-backup {{organization}} --token-from-gh {{[-O|--organization]}} --all {{[-o|--output-directory]}} {{path/to/directory}}`

- Back up only the issues and pull requests of a specific repository:

`github-backup {{username}} --token-from-gh {{[-R|--repository]}} {{repository}} --issues --pulls {{[-o|--output-directory]}} {{path/to/directory}}`

- Update an existing backup, fetching only what changed since the last run:

`github-backup {{username}} --token-from-gh --all {{[-i|--incremental]}} {{[-o|--output-directory]}} {{path/to/directory}}`
