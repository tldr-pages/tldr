# npm repo

> Open the repository page of a package in the browser.
> More information: <https://docs.npmjs.com/cli/npm-repo>.

- Open the repository page of the current project (based on `package.json`):

`npm repo`

- Open the repository page of a specific package from the registry:

`npm repo {{package_name}}`

- Open repository pages for multiple packages:

`npm repo {{package_name1 package_name2 ...}}`

- Print the repository URL instead of opening it in the browser:

`npm repo --browser false`

- Open the repository page for a package in a specific browser:

`npm repo --browser {{browser_name}}`

- Open the repository page of a package in a specific workspace:

`npm repo --workspace {{workspace_name}}`
