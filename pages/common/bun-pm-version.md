# bun pm version

> Manage the `version` field in `package.json`.
> More information: <https://bun.com/docs/pm/cli/pm#version>.

- Display the current package version:

`bun pm version`

- Set a specific version:

`bun pm version {{9.0.1}}`

- Bump the version using a semantic version type (`major`, `minor`, `patch`, etc.):

`bun pm version {{major|minor|patch|premajor|preminor|prepatch|prerelease}}`

- Set the version based on Git tags:

`bun pm version from-git`
