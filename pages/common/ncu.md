# ncu

> Find newer versions of package dependencies and check outdated npm packages locally or globally.
> `ncu` only updates dependency versions in `package.json`. To install the new versions, run `npm install` afterwards.
> More information: <https://github.com/raineorshine/npm-check-updates>.

- List outdated dependencies in the current directory:

`ncu`

- List outdated global npm packages:

`ncu --global`

- Upgrade all dependencies in the current directory:

`ncu --upgrade`

- Interactively upgrade dependencies in the current directory:

`ncu --interactive`

- List outdated dependencies up to the highest minor version:

`ncu --target {{minor}}`

- List outdated dependencies that match a keyword or regular expression:

`ncu --filter {{keyword|/regex/}}`

- List only a specific section of outdated dependencies:

`ncu --dep {{dev|optional|peer|prod|packageManager}}`

- Display help:

`ncu --help`
