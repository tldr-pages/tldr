# ncu

> Find newer versions of package dependencies and check outdated npm packages locally or globally.
> More information: <https://github.com/raineorshine/npm-check-updates>.

- Install npm package `node-check-updates` globally:

`npm install -g node-check-updates`

- List outdated npm packages in the current directory:

`ncu`

- List outdated global npm packages:

`ncu -g`

- Upgrade all npm packages in the current directory:

`ncu -u && npm install`

- Interactively upgrade npm packages in the current directory:

`ncu -i && npm install`

- Display help:

`ncu -h`
