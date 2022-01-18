# core-validate-commit

> Validate commit messages for Node.js core.
> More information: <https://github.com/nodejs/core-validate-commit>.

- Validate the current commit:

`core-validate-commit`

- Validate a specific commit:

`core-validate-commit {{commit_hash}}`

- Validate a range of commits:

`git rev-list {{commit_hash}}..HEAD | xargs core-validate-commit`

- List all validation rules:

`core-validate-commit --list`

- List all valid Node.js subsystems:

`core-validate-commit --list-subsystem`

- Validate the current commit formatting the output in tap format:

`core-validate-commit --tap`

- Display help:

`core-validate-commit --help`
