# nvm

> Install, uninstall or switch between Node.js versions.
> Supports version numbers like "0.12" or "v4.2", and labels like "stable", "system", etc.
> More information: <https://github.com/coreybutler/nvm-windows>.

- Install a specific version of Node.js:

`nvm install {{node_version}}`

- Sets the default version of Node.js (must be run as Administrator):

`nvm use {{node_version}}`

- List all available Node.js versions and highlight the default one:

`nvm list`

- Uninstall a given Node.js version:

`nvm uninstall {{node_version}}`

- Launch the REPL of a specific version of Node.js:

`node`

- Execute a script in a specific version of Node.js:

`node {{app.js}}`
