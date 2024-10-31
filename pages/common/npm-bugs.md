# npm bugs

> Report bugs for a package in a web browser.
> Attempts to open the package's bug tracker URL or support email.
> More information: <https://docs.npmjs.com/cli/npm-bugs>.

- Report bugs for a specific package-  Opens the bug tracker for the specified package:

`npm bugs {{pkgname}}`

- Open bug tracker for the current package-  Searches for a `package.json` and uses its name to open the bug tracker:

`npm bugs`

- Configure the browser used to open URLs-  Set the preferred browser for npm commands:

`npm config set browser {{browser_name}}`

- Suppress browser behavior-  Set to false to print URLs to the terminal instead of opening a browser:

`npm config set browser {{false}}`

- Use the default system URL opener-  Set to true to use the system's default method for opening URLs:

`npm config set browser {{true}}`
