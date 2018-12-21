# nvm

> Node.js version manager.
> Switch between NodeJS versions: system, node, 0.10, 0.12, 4.2 etc.

- Install a specific version of NodeJS:

`nvm install {{node_version}}`

- Use a specific version NodeJS in the current shell:

`nvm use {{node_version}}`

- Set the default NodeJS version:

`nvm alias default {{node_version}}`

- List all available NodeJS versions and print the default one:

`nvm list`

- Run a specific version NodeJS REPL:

`nvm run {{node_version}} --version`

- Run app in a specific version of NodeJS:

`nvm exec {{node_version}} node {{app.js}}`
