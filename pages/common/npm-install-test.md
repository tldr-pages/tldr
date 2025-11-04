# npm install-test

> Install dependencies and then run tests in a Node.js project.
> Equivalent to running `npm install` followed by `npm test`.
> More information: <https://docs.npmjs.com/cli/v8/commands/npm-install-test>.

- Install all dependencies and then run tests:

`npm {{[it|install-test]}}`

- Install a specific package and then run tests:

`npm {{[it|install-test]}} {{package_name}}`

- Install a package and save it as a dependency before running tests:

`npm {{[it|install-test]}} {{package_name}} {{[-S|--save]}}`

- Install dependencies globally and then run tests:

`npm {{[it|install-test]}} {{[-g|--global]}}`
