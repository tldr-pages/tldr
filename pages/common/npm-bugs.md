# npm bugs

> Report bugs for a package in a web browser.
> Attempts to open the package's bug tracker URL or support email.
> More information: <https://docs.npmjs.com/cli/npm-bugs>.

- Report bugs for a specific package by opening the bug tracker for the specified package:

`npm bugs {{package_name}}`

- Open the bug tracker for the current package by searching for a `package.json` file and using its name:

`npm bugs`

- Configure the browser used to open URLs by setting your preferred browser for `npm` commands:

`npm {{[c|config]}} set browser {{browser_name}}`

- Control URL opening: set `browser` to `true` for the system URL opener, or `false` to print URLs in the terminal:

`npm {{[c|config]}} set browser {{true|false}}`
