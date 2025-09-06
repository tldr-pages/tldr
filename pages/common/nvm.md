# nvm

> Install, uninstall or switch between Node.js versions.
> Supports version numbers like "12.8" or "v16.13.1", and labels like "stable", "system", etc.
> See also: `asdf`.
> More information: <https://github.com/creationix/nvm>.

- Install a specific version of Node.js:

`nvm install {{node_version}}`

- Use a specific version of Node.js in the current shell:

`nvm use {{node_version}}`

- Set the default Node.js version:

`nvm alias default {{node_version}}`

- List all available Node.js versions and highlight the default one:

`nvm list`

- Uninstall a given Node.js version:

`nvm uninstall {{node_version}}`

- Launch the REPL of a specific version of Node.js:

`nvm run {{node_version}} --version`

- Execute a script in a specific version of Node.js:

`nvm exec {{node_version}} node {{app.js}}`
