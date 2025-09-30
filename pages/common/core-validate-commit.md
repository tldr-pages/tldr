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

`core-validate-commit {{[-l|--list]}}`

- List all valid Node.js subsystems:

`core-validate-commit {{[-ls|--list-subsystem]}}`

- Validate the current commit formatting the output in tap format:

`core-validate-commit {{[-t|--tap]}}`

- Display help:

`core-validate-commit {{[-h|--help]}}`
