# bumpp

> Interactive CLI that bumps version numbers in package manifests, commits changes, and creates git tags.
> More information: <https://github.com/antfu-collective/bumpp>.

- Interactively prompt for a new version and update the current package manifest:

`bumpp`

- Bump the patch, minor, or major version directly without prompting:

`bumpp {{patch|minor|major}}`

- Bump the version across multiple files in a monorepo:

`bumpp {{package.json}} "{{packages/*/package.json}}"`

- Bump the version without creating a git commit, tag, or push:

`bumpp --no-commit --no-tag --no-push`
