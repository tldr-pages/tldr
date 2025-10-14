# npm diff

> Compare package versions from the `npm` registry and show differences.
> Similar to `git diff`.
> More information: <https://docs.npmjs.com/cli/npm-diff>.

- Compare two specific package versions:

`npm diff --diff {{package_name}}@{{version1}} --diff {{package_name}}@{{version2}}`

- Compare current local packages with latest published version:

`npm diff`

- Compare current local package with a specific version:

`npm diff --diff {{package_name}}@{{version}}`

- Compare a package in the current directory with the registry version:

`npm diff --diff {{package_name}}`

- Show only filenames that differ:

`npm diff --diff-name-only --diff {{package_name}}@{{version1}} --diff {{package_name}}@{{version2}}`

- Compare specific files or directories only:

`npm diff {{path/to/file_or_directory}} --diff {{package_name}}@{{version1}} --diff {{package_name}}@{{version2}}`

- Ignore whitespace when comparing:

`npm diff --diff-ignore-all-space --diff {{package_name}}@{{version1}} --diff {{package_name}}@{{version2}}`
