# npm install-test

> Equivalent to running `npm install` followed by `npm test`.
> Note: `it` can be used as shorthand for `install-test`.
> More information: <https://docs.npmjs.com/cli/npm-install-test>.

- Install all dependencies and then run tests:

`npm install-test`

- Install a specific package and then run tests:

`npm install-test {{package_name}}`

- Install a package and save it as a dependency before running tests:

`npm install-test {{package_name}} {{[-S|--save]}}`

- Install dependencies globally and then run tests:

`npm install-test {{[-g|--global]}}`
