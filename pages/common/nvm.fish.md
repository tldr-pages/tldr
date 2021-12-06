# nvm.fish

> Install, uninstall or switch between Node.js versions under the `fish` shell.
> Supports version numbers like "0.12" or "v4.2", and labels like "stable", "system", etc.
> More information: <https://github.com/jorgebucaran/nvm.fish>.

- Install a specific version of Node.js:

`nvm install {{node_version}}`

- Use a specific version of Node.js in the current shell:

`nvm use {{node_version}}`

- Set the default Node.js version:

`set nvm_default_version {{node_version}}`

- List all available Node.js versions and highlight the default one:

`nvm list`

- Uninstall a given Node.js version:

`nvm uninstall {{node_version}}`
