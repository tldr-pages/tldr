# npm version

> Bump a node package version.
> More information: <https://docs.npmjs.com/cli/commands/npm-version>.

- Check current version:

`npm version`

- Bump the minor version:

`npm version minor`

- Set a specific version:

`npm version {{version}}`

- Bump the patch version without creating a Git tag:

`npm version patch --no-git-tag-version`

- Bump the major version with a custom commit message:

`npm version major {{[-m|--message]}} "{{Upgrade to %s for reasons}}"`
